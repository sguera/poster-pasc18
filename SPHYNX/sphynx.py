import os
import reframe as rfm
import reframe.utility.sanity as sn


@rfm.simple_test
class SphynxCpuCheck(rfm.RunOnlyRegressionTest):
    def __init__(self, **kwargs):
        super().__init__('sphynx_cpu_check', os.path.dirname(__file__), **kwargs)
        self.descr = ('ReFrame Sphynx Evrard3D check')
        self.valid_systems = ['daint:gpu', 'dom:gpu']
        self.valid_prog_environs = ['PrgEnv-intel']
        self.sourcesdir = 'src/'

        self.modules = ['sphynx/1.4-CrayIntel-17.08']
        self.executable = '$EBROOTSPHYNX/evrard1M.exe'
        self.num_tasks = 4
        self.num_tasks_per_node = 1
        self.num_cpus_per_task = 12
        self.variables = {
            'OMP_NUM_THREADS': str(self.num_cpus_per_task),
            'MPICH_NO_BUFFER_ALIAS_CHECK': '1'
        }
        self.maintainers = ['JG']
        self.tags = {'sphexa'}

        self.pre_run = [
            'echo EBROOTSPHYNX=$EBROOTSPHYNX',
            'module list -t'
        ]

        self.outputtimes_file = 'conservelaws.d'
        self.sanity_patterns = sn.all([
            sn.assert_found('2.1000000000E-04', self.outputtimes_file)
        ])
