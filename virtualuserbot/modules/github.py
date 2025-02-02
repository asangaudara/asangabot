"""Get information about an user on GitHub
Syntax: .github USERNAME"""
import requests

from virtualuserbot import CMD_HELP
from virtualuserbot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@borg.on(friday_on_cmd("github (.*)"))
@borg.on(sudo_cmd("github (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://api.github.com/users/{}".format(input_str)
    r = requests.get(url)
    if r.status_code != 404:
        b = r.json()
        avatar_url = b["avatar_url"]
        html_url = b["html_url"]
        gh_type = b["type"]
        name = b["name"]
        company = b["company"]
        blog = b["blog"]
        location = b["location"]
        bio = b["bio"]
        created_at = b["created_at"]
        await borg.send_file(
            event.chat_id,
            caption="""Name: [{}]({})
Type: {}
Company: {}
Blog: {}
Location: {}
Bio: {}
Profile Created: {}""".format(
                name, html_url, gh_type, company, blog, location, bio, created_at
            ),
            file=avatar_url,
            force_document=False,
            allow_cache=False,
            reply_to=event,
        )
        await event.delete()
    else:
        await edit_or_reply(event, "`{}`: {}".format(input_str, r.text))


CMD_HELP.update(
    {
        "github": "**GitHub**\
\n\n**Syntax : **`.github <username>`\
\n**Usage :** Get information about an user on GitHub."
    }
)
