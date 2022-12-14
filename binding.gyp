{
  "targets": [
    {
      "target_name": "ci2c",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ "addons/ci2c.cc", "addons/i2c.c" ],
			'include_dirs': ["<!(node -p \"require('node-addon-api').include_dir\")"],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    },
		 {
      "target_name": "gstreamer-superficial",
      "sources": [ 
				"fork/node-gstreamer-superficial-master/gstreamer.cpp", 
				"fork/node-gstreamer-superficial-master/GLibHelpers.cpp", 
				"fork/node-gstreamer-superficial-master/GObjectWrap.cpp", 
				"fork/node-gstreamer-superficial-master/Pipeline.cpp" 
			],
	  "include_dirs": [
		"<!(node -e \"require('nan')\")"
	  ],
	  "cflags": [
	  	"-Wno-cast-function-type"
	  ],
	  "conditions" : [
		["OS=='linux'", {
			"include_dirs": [
				'<!@(pkg-config gstreamer-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)'
			],
			"libraries": [
				'<!@(pkg-config gstreamer-1.0 --libs)',
				'<!@(pkg-config gstreamer-app-1.0 --libs)',
				'<!@(pkg-config gstreamer-video-1.0 --libs)'
			]
		}],
		["OS=='mac'", {
			"include_dirs": [
				'<!@(pkg-config gstreamer-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)'
			],
			"libraries": [
				'<!@(pkg-config gstreamer-1.0 --libs)',
				'<!@(pkg-config gstreamer-app-1.0 --libs)',
				'<!@(pkg-config gstreamer-video-1.0 --libs)'
			]
		}],
		["OS=='win'", {
			"include_dirs": [
				"<!(echo %GSTREAMER_1_0_ROOT_MSVC_X86_64%)include\gstreamer-1.0",
				"<!(echo %GSTREAMER_1_0_ROOT_MSVC_X86_64%)lib\glib-2.0\include",
				"<!(echo %GSTREAMER_1_0_ROOT_MSVC_X86_64%)include\glib-2.0",
				"<!(echo %GSTREAMER_1_0_ROOT_MSVC_X86_64%)include\libxml2"
			],
			"libraries": [
				"<!(echo %GSTREAMER_1_0_ROOT_MSVC_X86_64%)lib\gstreamer-1.0.lib",
				"<!(echo %GSTREAMER_1_0_ROOT_MSVC_X86_64%)lib\gstapp-1.0.lib",
				"<!(echo %GSTREAMER_1_0_ROOT_MSVC_X86_64%)lib\gstvideo-1.0.lib",
				"<!(echo %GSTREAMER_1_0_ROOT_MSVC_X86_64%)lib\gobject-2.0.lib",
				"<!(echo %GSTREAMER_1_0_ROOT_MSVC_X86_64%)lib\glib-2.0.lib"
			]
		}]
	  ]
    }
  
  ]
}