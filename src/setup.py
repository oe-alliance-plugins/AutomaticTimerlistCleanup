from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.AutomaticTimerlistCleanup'
setup(name='enigma2-plugin-systemplugins-automatictimerlistcleanup',
       version='3.0',
       description='Automatic Timerlist Cleanup Plugin',
       package_dir={pkg: 'AutomaticTimerlistCleanup'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
