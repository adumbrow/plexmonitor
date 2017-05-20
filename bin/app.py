import web,os,statvfs

#Get disk information
disk = os.statvfs("/")

capacity = round(disk.f_bsize * disk.f_blocks / 1.073741824e9, 2)
available = round(disk.f_bsize * disk.f_bavail / 1.073741824e9, 2)
used = round(disk.f_bsize * (disk.f_blocks - disk.f_bavail) / 1.073741824e9, 2)

urls = (
  '/', 'Index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')


class Index(object):
    def GET(self):
        return render.index(capacity = capacity, available = available, used = used)

if __name__ == "__main__":
    app.run()
