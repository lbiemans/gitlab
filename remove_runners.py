import gitlab
TOKEN=""
URL=""
gl = gitlab.Gitlab(URL, private_token=TOKEN)
for x in range(0, 5000):
    try:
        gl.runners.delete(x)
    except:
        pass
