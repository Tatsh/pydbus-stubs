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
