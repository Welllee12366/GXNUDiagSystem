# -*- coding:utf-8 -*-
from GXNUDiagSystem import GXNUDiagSystem
if __name__ == '__main__':
    diag = GXNUDiagSystem()
    diag.login()
    print(diag.checkAlive())