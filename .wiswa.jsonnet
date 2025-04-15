local utils = import 'utils.libjsonnet';

(import 'defaults.libjsonnet') + {
  // Project-specific
  description: 'PEP 561 type stubs for pydbus.',
  keywords: ['dbus', 'pep561', 'stubs', 'types'],
  project_name: 'pydbus-stubs',
  version: '0.0.3',
  citation+: {
    'date-released': '2025-04-15',
  },
  want_docs: false,
  want_tests: false,
  stubs_only: true,
  primary_module: 'pydbus-stubs',
  pyproject+: {
    tool+: {
      poetry+: {
        dependencies+: {
          'pygobject-stubs': '^2.13.0',
        },
        group+: {
          dev+: {
            dependencies+: {
              pydbus: '^0.6.0',
              pygobject: '^3.52.3',
            },
          },
        },
      },
    },
  },
  // Common
  authors: [
    {
      'family-names': 'Udvare',
      'given-names': 'Andrew',
      email: 'audvare@gmail.com',
      name: '%s %s' % [self['given-names'], self['family-names']],
    },
  ],
  local funding_name = '%s2' % std.asciiLower(self.github_username),
  github_username: 'Tatsh',
  github+: {
    funding+: {
      ko_fi: funding_name,
      liberapay: funding_name,
      patreon: funding_name,
    },
  },
}
