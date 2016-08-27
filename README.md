# Sublime Text - WDB
Simple python wdb debugger plugin

# Dependencies
Install [wdb](https://github.com/Kozea/wdb) first.

# Install
Now, this plugin is very inferior.

- Ubuntu
    ``` bash
    # chdir sublime text package directory
    $ cd ~/.config/sublime-text-3/Packages

    # clone this repo
    $ git clone https://github.com/Ashon/sublime-wdb
    ```

# Usage
Open Command Pallet (`ctrl` + `shift` + `p`)
type `wdb`

![commandPallete](https://raw.githubusercontent.com/ashon/sublime-wdb/master/assets/wdb_in_sublime.png)

# Use `Python Breakpoints` plugin and change default debugger.
If you uses `python breakpoints`, change default debugger to wdb.
```
{
  // preferred debugger (pdb, ipdb, pudb,..) - must support set_trace() call
  "debugger": "wdb",

  // "auto" (read from global settings), or a positive integer
  "tab_size": "auto",

  // name of scope for color highlighting; replace with "mark" if "invalid" is annoying
  "highlight": "invalid",

  // icon name for the gutter, one of: "" (disabled), "dot", "circle", "bookmark" or "cross"
  "gutter_icon": "circle",

  // auto-save the file on breakpoint toggle
  "save_on_toggle": false
}
```

Then make breakepoint in your python code. (`ctrl` + `shift` + `b`)

![pythonBreakPoints](https://raw.githubusercontent.com/ashon/sublime-wdb/master/assets/use_python_breakpoints.png)
