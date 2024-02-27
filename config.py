class bot:
    prefix = '!'


class roles:
    support = 775778822334709788


tesseract_cmd = 'tesseract'

plugins = {
    'api': {
        'url': 'https://modrinth.com/plugin/limboapi/versions',
        'title': 'LimboAPI'
    },
    'auth': {
        'url': 'https://modrinth.com/plugin/limboauth/versions',
        'title': 'LimboAuth'
    },
    'filter': {
        'url': 'https://modrinth.com/plugin/limbofilter/versions',
        'title': 'LimboFilter'
    },
    'hub': {
        'url': 'https://modrinth.com/plugin/limbohub/versions',
        'title': 'LimboHub'
    },
    'addon': {
        'url': 'https://modrinth.com/plugin/limboauth-socialaddon/versions',
        'title': 'LimboAuth-SocialAddon'
    },
    'reconnect': {
        'url': 'https://modrinth.com/plugin/limboreconnect/versions',
        'title': 'LimboReconnect'
    }
}
velocity_link = 'https://api.papermc.io/v2/projects/velocity/versions/3.3.0-SNAPSHOT/builds/{build}/downloads/velocity-3.3.0-SNAPSHOT-{build}.jar'
