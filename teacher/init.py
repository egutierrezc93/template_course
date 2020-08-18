course_id = 'XXXXXXXX'
github_repo = 'XXXXXX/%s'%course_id
zip_file_url="https://github.com/%s/archive/master.zip"%github_repo
endpoint = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'


def get_last_modif_date(localdir):
    try:
        import time, os, pytz
        import datetime
        k = datetime.datetime.fromtimestamp(max(os.path.getmtime(root) for root,_,_ in os.walk(localdir)))
        localtz = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
        k = k.astimezone(localtz)
        return k
    except Exception:
        return None
    
import requests, zipfile, io, os, shutil, subprocess
def init(force_download=False):

    install_sourcedefender()

    if force_download or not os.path.exists("local"):
        print("replicating local resources")
        dirname = course_id+"-master/"
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
        r = requests.get(zip_file_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
        if os.path.exists("local"):
            shutil.rmtree("local")
        shutil.move(dirname+"/local", "local")
        shutil.rmtree(dirname)

def get_weblink():
    from IPython.display import HTML
    print ("endpoint", endpoint)
    return HTML("<h3>See <a href='"+endpoint+"/web/login' target='_blank'>my courses and progress</a></h2>")

def install_sourcedefender():
    print('Installing sourcedefender...')
    output = subprocess.run(['pip', 'install', 'sourcedefender'], stderr=subprocess.PIPE)

    if output.returncode != 0:
        STDOUT_RED_COLOR = '\033[91m'
        STDOUT_RESET_COLOR = '\033[0m'
        print('Sourcedefender installation failed, returning')
        print(STDOUT_RED_COLOR + output.stderr.decode('ASCII') + STDOUT_RESET_COLOR)
    else:
       print('Successfully installed')

