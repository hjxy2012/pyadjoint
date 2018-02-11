from fenics_adjoint.assembly import assemble, assemble_system
from fenics_adjoint.solving import solve
from fenics_adjoint.projection import project
from fenics_adjoint.types import Constant, DirichletBC, FunctionSpace
from fenics_adjoint.variational_solver import (NonlinearVariationalProblem, NonlinearVariationalSolver,
                                               LinearVariationalProblem, LinearVariationalSolver)

from firedrake_adjoint.types.expression import Expression
from firedrake_adjoint.types.function import Function

from pyadjoint.tape import (Tape, set_working_tape, get_working_tape,
                            pause_annotation, continue_annotation)
from pyadjoint.reduced_functional import ReducedFunctional
from pyadjoint.verification import taylor_test
from pyadjoint.drivers import compute_gradient, compute_hessian 
from pyadjoint.adjfloat import AdjFloat
from pyadjoint.control import Control

tape = Tape()
set_working_tape(tape)
