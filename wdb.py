
import sublime, sublime_plugin
import subprocess
import webbrowser

WDB_SERVER_ATTR = 'wdb_server'
SUBPROCESS_CMD = 'wdb.server.py'


class wdb_run_server(sublime_plugin.TextCommand):

    def run(self, edit):
        WdbServerSubprocessThread.run()

    def description(self):
        return 'run wdb server'


class wdb_kill_server(sublime_plugin.TextCommand):

    def run(self, edit):
        WdbServerSubprocessThread.stop()


class wdb_open_in_browser(sublime_plugin.TextCommand):

    def run(self, edit):
        webbrowser.open_new('http://localhost:1984')


class WdbServerSubprocessThread(object):

    @staticmethod
    def run():

        try:
            existing_wdb_server = getattr(sublime, WDB_SERVER_ATTR, None)

            if existing_wdb_server is None:

                wdb_server_instance = subprocess.Popen(SUBPROCESS_CMD)
                setattr(sublime, WDB_SERVER_ATTR, wdb_server_instance)

                print('wdb server running')

            else:
                print('wdb server already running')

        except Exception as e:
            print(e)

    @staticmethod
    def stop():
        try:

            wdb_server = getattr(sublime, WDB_SERVER_ATTR, None)

            if wdb_server:
                wdb_server.kill()
                del wdb_server
                delattr(sublime, WDB_SERVER_ATTR)

                print('wdb server stopped')

            else:
                print('wdb server already stopped')

        except Exception as e:
            print(e)
