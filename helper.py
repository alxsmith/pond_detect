from dotenv import dotenv_values

def planet_auth(key="PL_API_KEY"):
  """_summary_

  Parameters
  ----------
  key : str, optional
      _description_, by default "PL_API_KEY"
  """  
  # Get your Planet API Key from an environment variable
  DOT_ENV_VALS = dotenv_values(".env")
  # Your Planet API Key
  API_KEY = DOT_ENV_VALS["PL_API_KEY"]
  return API_KEY