import dominate
from dominate import tags as dtags

doc = dominate.document(title="TKP")

with doc.head:
    dtags.link(rel="stylesheet", href="style.css", type="text/css")
    with open("gtag.html", "r") as gtag:
        content = gtag.read()
    # print(content)
    dominate.util.raw(content)

with doc:
    with dtags.div(id='header').add(dtags.ol()):
        for i in ['home', 'about', 'contact']:
            dtags.li(dtags.a(i.title(), href='/%s.html' % i))

    with dtags.div():
        dtags.attr(cls='body')
        dtags.p('Lorem ipsum..')

print(doc)
