#!/usr/bin/env python
# *-* coding: utf-8 *-*

from github3 import login
import base64

gh = login(username="ST4LK3RCR4ZY",password="91284567qwer")
repo = gh.repository("ST4LK3RCR4ZY", "qualquer")
branch = repo.branch("master")

#repo.create_file(a,"Commit message",base64.b64encode(a))

with open("/root/Imagens/fora.png", "rb") as f:
    data = f.read()
    repo.create_file("arquivo.jpg","Commit message", data)
