local utils = import 'utils.libjsonnet';

{
  description: 'PEP 561 type stubs for pydbus.',
  keywords: ['dbus', 'pep561', 'stubs', 'types'],
  project_name: 'pydbus-stubs',
  version: '0.0.3',
  want_docs: false,
  want_tests: false,
  stubs_only: true,
  primary_module: self.project_name,
  local apt_packages = ['libcairo2-dev', 'libgirepository-2.0-dev'],
  github+: {
    workflows+: {
      qa+: {
        apt_packages: apt_packages,
      },
    },
  },
  pyproject+: {
    tool+: {
      poetry+: {
        dependencies+: {
          'pygobject-stubs': utils.latestPypiPackageVersionCaret('pygobject-stubs'),
        },
        group+: {
          dev+: {
            dependencies+: {
              pydbus: utils.latestPypiPackageVersionCaret('pydbus'),
              pygobject: utils.latestPypiPackageVersionCaret('pygobject'),
            },
          },
        },
      },
    },
  },
}
