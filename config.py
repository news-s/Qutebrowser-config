config.load_autoconfig(False)

path_to_start_page = "path"


c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = "dark"
c.statusbar.show = "in-mode"
c.tabs.show = "switching"
c.tabs.position = "top"
c.tabs.favicons.show = "pinned"
c.url.start_pages = path_to_start_page


c.url.searchengines = {
    "DEFAULT": "https://google.com/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "git": "https://github.com/search?q={}",
    "stack": "https://stackoverflow.com/search?q={}",
    #since im not playing lol anymore "lol": "u.gg/lol/champions/{}/build",
    "arch": "https://wiki.archlinux.org/?search={}", #because of this
}

config.bind('j', 'tab-prev')
config.bind('k', 'tab-next')
config.bind('X', 'undo')
config.bind('<Ctrl-t>', f'open -t {path_to_start_page}')

c.aliases['chat'] = 'open -t https://chat.openai.com'

c.content.javascript.enabled = True
c.content.autoplay = False
c.content.cookies.accept = "no-3rdparty"
c.content.geolocation = False
c.content.notifications.enabled = False

c.content.blocking.enabled = True
c.content.blocking.method = "both"
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt"
]

c.editor.command = ["code", "{}"]
