# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/04_lmu_dms.ipynb (unless otherwise specified).

__all__ = ['LDN', 'make_ldn_B_A', 'make_lmu_dms']

# Cell
import numpy as np
import nengo
import scipy.linalg


class LDN(nengo.Process):
    def __init__(self, theta, q, size_in=1):
        self.q = q              # number of internal state dimensions per input
        self.theta = theta      # size of time window (in seconds)
        self.size_in = size_in  # number of inputs

        # Do Aaron's math to generate the matrices
        #  https://github.com/arvoelke/nengolib/blob/master/nengolib/synapses/analog.py#L536
        Q = np.arange(q, dtype=np.float64)
        R = (2*Q + 1)[:, None] / theta
        j, i = np.meshgrid(Q, Q)

        self.A = np.where(i < j, -1, (-1.)**(i-j+1)) * R
        self.B = (-1.)**Q[:, None] * R

        super().__init__(default_size_in=size_in, default_size_out=q*size_in)

    def make_step(self, shape_in, shape_out, dt, rng, state=None):
        state = np.zeros((self.q, self.size_in))

        # Handle the fact that we're discretizing the time step
        #  https://en.wikipedia.org/wiki/Discretization#Discretization_of_linear_state_space_models
        Ad = scipy.linalg.expm(self.A*dt)
        Bd = np.dot(np.dot(np.linalg.inv(self.A), (Ad-np.eye(self.q))), self.B)

        # this code will be called every timestep
        def step_legendre(t, x, state=state):
            state[:] = np.dot(Ad, state) + np.dot(Bd, x[None, :])
            return state.T.flatten()
        return step_legendre


# Cell

def make_ldn_B_A(theta=6.0, q=6, size_in=2):
    ldn = LDN(theta=theta, q=q, size_in=2)
    B_full = np.zeros((ldn.q*size_in, size_in))
    A_full = np.zeros((ldn.q*size_in, ldn.q*size_in))
    for i in range(size_in):
        B_full[ldn.q*i:ldn.q*(i+1), i:i+1] = ldn.B
        A_full[ldn.q*i:ldn.q*(i+1), ldn.q*i:ldn.q*(i+1)] = ldn.A

    return ldn, B_full, A_full


# Cell
from .dms import DMSTask


def make_lmu_dms(theta=6.0, q=6, n_neurons=3000, seed=1337,
                 out_transform=None,
                 n_trials_per_cond=5, trial_seed=1337,
                 tau=0.1):
    """
    Make a LMU network that performs the delayed match to sample task.
    returns the model and a dictionary of the probes.
    """
    ldn, B_full, A_full = make_ldn_B_A(theta=theta, q=q, size_in=2)
    dms = DMSTask(gen_trials_per_cond=n_trials_per_cond, cond_seed=trial_seed)

    model = nengo.Network()
    with model:
        stim = nengo.Node(dms.stim_signal)

        ens = nengo.Ensemble(n_neurons=n_neurons, dimensions=ldn.q*2, seed=seed)

        nengo.Connection(stim, ens, transform=B_full*tau, synapse=tau)
        nengo.Connection(ens, ens, synapse=tau, transform=A_full*tau+np.eye(ldn.q*2))

        output = nengo.Node(None, size_in=1)
        if out_transform is None:
            out_transform = np.ones((1, ens.n_neurons))
        nengo.Connection(ens.neurons, output,
                         transform=out_transform)

        # Sim the 'ideal' signal.
        ideal = nengo.Node(dms.ideal_signal)

        # Capture the output
        probes = {
            'ensemble': nengo.Probe(ens.neurons),
            'output': nengo.Probe(output),
            'ideal': nengo.Probe(ideal)
        }
    return model, probes