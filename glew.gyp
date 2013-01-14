# Copyright cybertk. kyan.ql.he@gmail.com
{
  'variables': {
    'conditions': [
      ['OS == "linux"', {
        'use_system_glew': 1,
      }, {
        'use_system_glew': 0,
      }],
    ],
  },

  'conditions': [
    ['use_system_glew == 1', {
      'targets': [
        {
          'target_name': 'glew',
          'type': 'none',
          'link_settings': {
            'libraries': [
              '-lGLEW',
            ],
          },
        }, # target
      ],
    }, { # else: use_system_glew != 1
      'targets': [
        {
          'target_name': 'glew',
            # TODO(kyan): Provide shared_library support.
          'type': 'static_library',

          'direct_dependent_settings': {
            'include_dirs': [
              'files/glew-1.9.0/include',
            ],
            'defines': [
              'GLEW_STATIC',
            ],
          }, # direct_dependent_settings

          'msvs_settings': {
            'VCCLCompilerTool': {
              'CompileAs': '1',
              #'DisableSpecificWarnings': '4996',
            },
            'VCLibrarianTool': {
              # pragma in code explictly use glew_static.lib.
              'OutputFile': '<(PRODUCT_DIR)/lib/glew_static.lib',
            }
          }, # msvs_settings

          'include_dirs': [
            'files/glew-1.9.0/include',
          ],

          'sources': [
            'files/glew-1.9.0/src/glew.c',
            #'files/glew-1.9.0/src/glewinfo.c',
            #'files/glew-1.9.0/src/visualinfo.c',
          ], # sources

          'conditions': [
            [ 'OS == "win"', {
              'defines': [
                'GLEW_STATIC',
                '_LIB',
              ],
            }],
          ], # conditions
        },
      ]
    }], # conditions
  ],
}
