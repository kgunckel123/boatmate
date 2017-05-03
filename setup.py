from cx_Freeze import setup, Executable

includefiles = ['templates/','static/','boat_data.json']

base = None

main_executable = Executable("matrix_ex.py", base=base, copyDependentFiles=True)

setup(name="Boatmate_Schedule",
      version="0.1",
      description="",
      options={
      'build_exe': {
          'packages': ['helper_functions','model','forms'],
          'include_files': includefiles,
          'include_msvcr': True}},
      executables=[main_executable], requires=['flask'])