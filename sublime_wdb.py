
import sublime
import sublime_plugin
import subprocess
import webbrowser

WDB_SERVER_ATTR = 'wdb_server'
WDB_SERVER_URL = 'http://localhost:1984'
SUBPROCESS_CMD = 'wdb.server.py'


class wdb_run_server(sublime_plugin.TextCommand):

    def run(self, edit):
        WdbServerSubprocessThread.run()


class wdb_kill_server(sublime_plugin.TextCommand):

    def run(self, edit):
        WdbServerSubprocessThread.stop()


class wdb_open_in_browser(sublime_plugin.TextCommand):

    def run(self, edit):
        if WdbServerSubprocessThread.get_wdb_server():
            webbrowser.open_new(WDB_SERVER_URL)

        else:
            print('wdb server is not running')


class WdbServerSubprocessThread(object):

    @staticmethod
    def run():

        try:
            if WdbServerSubprocessThread.get_wdb_server() is None:

                wdb_server_instance = subprocess.Popen(SUBPROCESS_CMD)
                setattr(sublime, WDB_SERVER_ATTR, wdb_server_instance)

                print('wdb server running')

            else:
                print('wdb server already running')

        except Exception as e:
            print(e)


    @staticmethod
    def get_wdb_server():
        return getattr(sublime, WDB_SERVER_ATTR, None)


    @staticmethod
    def stop():
        try:
            wdb_server = WdbServerSubprocessThread.get_wdb_server()

            if wdb_server:

                wdb_server.kill()
                del wdb_server
                delattr(sublime, WDB_SERVER_ATTR)

                print('wdb server stopped')

            else:
                print('wdb server already stopped')

        except Exception as e:
            print(e)
