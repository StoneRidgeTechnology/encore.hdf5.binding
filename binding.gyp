{
    "variables": {
        "hdf5_home_linux%": '<!(node step/hdf5find.s)',
        "hdf5_home_win%": '<!(node step/hdf5find.s)',
        "hdf5_home_mac%": '<!(node step/hdf5find.s)',

        "link_type%": "shared",
        "debug_mode%": "",
        "longlong_type%": "LONGLONG64BITS"
    },
    'targets': [
        {
            'target_name': 'hdf5',
            'win_delay_load_hook': 'false',
            'conditions': [
            ['OS=="linux"', {
                'cflags!': [ '-fno-exceptions' ],
                'cflags_cc!': [ '-fno-exceptions' ],
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'include_dirs': [
                    '<(hdf5_home_linux)/include',
                    "/usr/include/hdf5/serial"
                ],
                'sources': [
                    'cpp/int64.cc',
                    'cpp/uint64.cc',
                    'cpp/hdf5.cc',
                    'cpp/attributes.cc',
                    'cpp/methods.cc',
                    'cpp/h5_file.cc',
                    'cpp/h5_group.cc',
                    'cpp/reference.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_linux)/lib'
                    ]
                }
            }],
            ['OS=="win"', {
				'defines': [
					'H5_BUILT_AS_DYNAMIC_LIB'
				],
                'include_dirs': [
                    '<(hdf5_home_win)/include',
                    './win/include',
                    './cpp',
                    'C:/Program Files/Microsoft SDKs/Windows/v7.1/Include'
                ],
                'sources': [
                    'cpp/int64.cc',
                    'cpp/uint64.cc',
                    'cpp/hdf5.cc',
                    'cpp/attributes.cc',
                    'cpp/methods.cc',
                    'cpp/h5_file.cc',
                    'cpp/h5_group.cc',
                    'cpp/reference.cc'
                ],
                "configurations": {
                            "Release": {
                    'msvs_settings':
                    {
                        'VCCLCompilerTool':
                        {
                            'RuntimeLibrary': 2,        # shared release
                            'ExceptionHandling': 1,     # /EHsc
                            'AdditionalOptions':
                            [
                                '/EHsc' # Enable unwind semantics for Exception Handling.  This one actually does the trick - and no warning either.
                            ]
                        },
                        'VCLinkerTool':
                        {
                            'AdditionalOptions':
                            [
                                '/FORCE:MULTIPLE'
                            ]
                        }
                    }
                }
                },
                'link_settings': {
                    'libraries': [
                        '<(hdf5_home_win)/lib/hdf5.lib',
                        '<(hdf5_home_win)/lib/hdf5_hl.lib'
                    ]
                }
            }],
            ['OS=="mac"', {
                'cflags!': [ '-fno-exceptions' ],
                'cflags_cc!': [ '-fno-exceptions' ],
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'xcode_settings': {
                    'OTHER_CPLUSPLUSFLAGS': ["-fPIC", "-<(link_type)", "-O3", "-std=c++14", "-fexceptions", "-stdlib=libc++"],
                    'OTHER_LDFLAGS': []
                },
                'include_dirs': [
                    '<(hdf5_home_mac)/include'
                ],
                'sources': [
                    'cpp/int64.cc',
                    'cpp/uint64.cc',
                    'cpp/hdf5.cc',
                    'cpp/attributes.cc',
                    'cpp/methods.cc',
                    'cpp/h5_file.cc',
                    'cpp/h5_group.cc',
                    'cpp/reference.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ]
                }
            }]
          ]
        },
        {
            'target_name': 'h5lt',
            'win_delay_load_hook': 'false',
            'conditions': [
            ['OS=="linux"', {
                'cflags!': [ '-fno-exceptions' ],
                'cflags_cc!': [ '-fno-exceptions' ],
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'include_dirs': [
                    '<(hdf5_home_linux)/include',
                    "/usr/include/hdf5/serial"
                ],
                'sources': [
                    'cpp/int64.cc',
                    'cpp/uint64.cc',
                    'cpp/h5lt.cc',
                    'cpp/reference.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_linux)/lib'
                    ]
                }
            }],
            ['OS=="win"', {
                'defines': [
					'H5_BUILT_AS_DYNAMIC_LIB'
				],
                'include_dirs': [
                    '<(hdf5_home_win)/include',
                    './win/include',
                    './cpp',
                    'C:/Program Files/Microsoft SDKs/Windows/v7.1/Include'
                ],
                'sources': [
                    'cpp/int64.cc',
                    'cpp/uint64.cc',
                    'cpp/reference.cc',
                    'cpp/h5lt.cc'
                ],
                "configurations": {
                            "Release": {
                    'msvs_settings':
                    {
                        'VCCLCompilerTool':
                        {
                            'RuntimeLibrary': 2,        # shared release
                            'ExceptionHandling': 1,     # /EHsc
                            'AdditionalOptions':
                            [
                                '/EHsc' # Enable unwind semantics for Exception Handling.  This one actually does the trick - and no warning either.
                            ]
                        },
                        'VCLinkerTool':
                        {
                            'AdditionalOptions':
                            [
                                '/FORCE:MULTIPLE'
                            ]
                        }
                    }
                }
                },
                'link_settings': {
                    'libraries': [
                        '<(hdf5_home_win)/lib/hdf5.lib',
                        '<(hdf5_home_win)/lib/hdf5_hl.lib'
                    ],
                }
            }],
            ['OS=="mac"', {
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'xcode_settings': {
                    'OTHER_CPLUSPLUSFLAGS': ["-fPIC", "-<(link_type)", "-O3", "-std=c++14", "-fexceptions", "-stdlib=libc++"],
                    'OTHER_LDFLAGS': []
                },
                'include_dirs': [
                    '<(hdf5_home_mac)/include'
                ],
                'sources': [
                    'cpp/int64.cc',
                    'cpp/uint64.cc',
                    'cpp/h5lt.cc',
                    'cpp/reference.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ]
                }
            }]
          ]
        },
        {
            'target_name': 'h5tb',
            'win_delay_load_hook': 'false',
            'conditions': [
            ['OS=="linux"', {
                'cflags!': [ '-fno-exceptions' ],
                'cflags_cc!': [ '-fno-exceptions' ],
                'cflags': ["-D<(longlong_type)", "-fPIC", "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'include_dirs': [
                    '<(hdf5_home_linux)/include',
                    "/usr/include/hdf5/serial"
                ],
                'sources': [
                    'cpp/h5tb.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_linux)/lib'
                    ]
                }
            }],
            ['OS=="win"', {
                'defines': [
					'H5_BUILT_AS_DYNAMIC_LIB',
                                        "<(longlong_type)"
				],
                'include_dirs': [
                    '<(hdf5_home_win)/include',
                    './win/include',
                    './cpp',
                    'C:/Program Files/Microsoft SDKs/Windows/v7.1/Include'
                ],
                'sources': [
                    'cpp/h5tb.cc'
                ],
                "configurations": {
                            "Release": {
                    'msvs_settings':
                    {
                        'VCCLCompilerTool':
                        {
                            'RuntimeLibrary': 2,        # shared release
                            'ExceptionHandling': 1,     # /EHsc
                            'AdditionalOptions':
                            [
                                '/EHsc' # Enable unwind semantics for Exception Handling.  This one actually does the trick - and no warning either.
                            ]
                        },
                        'VCLinkerTool':
                        {
                            'AdditionalOptions':
                            [
                                '/FORCE:MULTIPLE'
                            ]
                        }
                    }
                }
                },
                'link_settings': {
                    'libraries': [
                        '<(hdf5_home_win)/lib/hdf5.lib',
                        '<(hdf5_home_win)/lib/hdf5_hl.lib'
                    ],
                }
            }],
            ['OS=="mac"', {
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'xcode_settings': {
                    'OTHER_CPLUSPLUSFLAGS': ["-D<(longlong_type)", "-fPIC", "-<(link_type)", "-O3", "-std=c++14", "-fexceptions", "-stdlib=libc++"],
                    'OTHER_LDFLAGS': []
                },
                'include_dirs': [
                    '<(hdf5_home_mac)/include'
                ],
                'sources': [
                    'cpp/h5tb.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ]
                }
            }]
          ]
        },
        {
            'target_name': 'h5pt',
            'win_delay_load_hook': 'false',
            'conditions': [
            ['OS=="linux"', {
                'cflags!': [ '-fno-exceptions' ],
                'cflags_cc!': [ '-fno-exceptions' ],
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'include_dirs': [
                    '<(hdf5_home_linux)/include',
                    "/usr/include/hdf5/serial"
                ],
                'sources': [
                    'cpp/int64.cc',
                    'cpp/uint64.cc',
                    'cpp/h5pt.cc',
                    'cpp/h5_pt.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_linux)/lib'
                    ]
                }
            }],
            ['OS=="win"', {
                'defines': [
					'H5_BUILT_AS_DYNAMIC_LIB'
				],
                'include_dirs': [
                    '<(hdf5_home_win)/include',
                    './win/include',
                    './cpp',
                    'C:/Program Files/Microsoft SDKs/Windows/v7.1/Include'
                ],
                'sources': [
                    'cpp/int64.cc',
                    'cpp/uint64.cc',
                    'cpp/h5pt.cc',
                    'cpp/h5_pt.cc'
                ],
                "configurations": {
                            "Release": {
                    'msvs_settings':
                    {
                        'VCCLCompilerTool':
                        {
                            'RuntimeLibrary': 2,        # shared release
                            'ExceptionHandling': 1,     # /EHsc
                            'AdditionalOptions':
                            [
                                '/EHsc' # Enable unwind semantics for Exception Handling.  This one actually does the trick - and no warning either.
                            ]
                        },
                        'VCLinkerTool':
                        {
                            'AdditionalOptions':
                            [
                                '/FORCE:MULTIPLE'
                            ]
                        }
                    }
                }
                },
                'link_settings': {
                    'libraries': [
                        '<(hdf5_home_win)/lib/hdf5.lib',
                        '<(hdf5_home_win)/lib/hdf5_hl.lib'
                    ],
                }
            }],
            ['OS=="mac"', {
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'xcode_settings': {
                    'OTHER_CPLUSPLUSFLAGS': ["-fPIC", "-<(link_type)", "-O3", "-std=c++14", "-fexceptions", "-stdlib=libc++"],
                    'OTHER_LDFLAGS': []
                },
                'include_dirs': [
                    '<(hdf5_home_mac)/include'
                ],
                'sources': [
                    'cpp/h5pt.cc',
                    'cpp/h5_pt.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ]
                }
            }]
          ]
        },
        {
            'target_name': 'h5im',
            'win_delay_load_hook': 'false',
            'conditions': [
            ['OS=="linux"', {
                'cflags!': [ '-fno-exceptions' ],
                'cflags_cc!': [ '-fno-exceptions' ],
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'include_dirs': [
                    '<(hdf5_home_linux)/include',
                    "/usr/include/hdf5/serial"
                ],
                'sources': [
                    'cpp/h5im.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_linux)/lib'
                    ]
                }
            }],
            ['OS=="win"', {
                'defines': [
					'H5_BUILT_AS_DYNAMIC_LIB'
				],
                'include_dirs': [
                    '<(hdf5_home_win)/include',
                    './win/include',
                    './cpp',
                    'C:/Program Files/Microsoft SDKs/Windows/v7.1/Include'
                ],
                'sources': [
                    'cpp/h5im.cc'
                ],
                "configurations": {
                            "Release": {
                    'msvs_settings':
                    {
                        'VCCLCompilerTool':
                        {
                            'RuntimeLibrary': 2,        # shared release
                            'ExceptionHandling': 1,     # /EHsc
                            'AdditionalOptions':
                            [
                                '/EHsc' # Enable unwind semantics for Exception Handling.  This one actually does the trick - and no warning either.
                            ]
                        },
                        'VCLinkerTool':
                        {
                            'AdditionalOptions':
                            [
                                '/FORCE:MULTIPLE'
                            ]
                        }
                    }
                }
                },
                'link_settings': {
                    'libraries': [
                        '<(hdf5_home_win)/lib/hdf5.lib',
                        '<(hdf5_home_win)/lib/hdf5_hl.lib'
                    ],
                }
            }],
            ['OS=="mac"', {
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'xcode_settings': {
                    'OTHER_CPLUSPLUSFLAGS': ["-fPIC", "-<(link_type)", "-O3", "-std=c++14", "-fexceptions", "-stdlib=libc++"],
                    'OTHER_LDFLAGS': []
                },
                'include_dirs': [
                    '<(hdf5_home_mac)/include'
                ],
                'sources': [
                    'cpp/h5im.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ]
                }
            }]
          ]
        },
        {
            'target_name': 'h5ds',
            'win_delay_load_hook': 'false',
            'conditions': [
            ['OS=="linux"', {
                'cflags!': [ '-fno-exceptions' ],
                'cflags_cc!': [ '-fno-exceptions' ],
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'include_dirs': [
                    '<(hdf5_home_linux)/include',
                    "/usr/include/hdf5/serial"
                ],
                'sources': [
                    'cpp/h5ds.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_linux)/lib'
                    ]
                }
            }],
            ['OS=="win"', {
                'defines': [
					'H5_BUILT_AS_DYNAMIC_LIB'
				],
                'include_dirs': [
                    '<(hdf5_home_win)/include',
                    './win/include',
                    './cpp',
                    'C:/Program Files/Microsoft SDKs/Windows/v7.1/Include'
                ],
                'sources': [
                    'cpp/h5ds.cc'
                ],
                "configurations": {
                            "Release": {
                    'msvs_settings':
                    {
                        'VCCLCompilerTool':
                        {
                            'RuntimeLibrary': 2,        # shared release
                            'ExceptionHandling': 1,     # /EHsc
                            'AdditionalOptions':
                            [
                                '/EHsc' # Enable unwind semantics for Exception Handling.  This one actually does the trick - and no warning either.
                            ]
                        },
                        'VCLinkerTool':
                        {
                            'AdditionalOptions':
                            [
                                '/FORCE:MULTIPLE'
                            ]
                        }
                    }
                }
                },
                'link_settings': {
                    'libraries': [
                        '<(hdf5_home_win)/lib/hdf5.lib',
                        '<(hdf5_home_win)/lib/hdf5_hl.lib'
                    ],
                }
            }],
            ['OS=="mac"', {
                'cflags': ['-fPIC', "-<(link_type)", "-O4", "-std=c++14", "-fexceptions", "-Werror", "-Wno-cast-function-type"],
                'xcode_settings': {
                    'OTHER_CPLUSPLUSFLAGS': ["-fPIC", "-<(link_type)", "-O3", "-std=c++14", "-fexceptions", "-stdlib=libc++"],
                    'OTHER_LDFLAGS': []
                },
                'include_dirs': [
                    '<(hdf5_home_mac)/include'
                ],
                'sources': [
                    'cpp/h5ds.cc'
                ],
                'link_settings': {
                    'libraries': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ],
                    'ldflags': [
                        '-L<(hdf5_home_mac)/lib',
                        '-lhdf5',
                        '-lhdf5_hl'
                    ]
                }
            }]
          ]
        }

    ]
}
