#!/usr/bin/env python
import os
import sys
# 사이트 관리를 도와주는 역. 다른 설치 없이 바로 웹서버를 시작할수 있음

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
