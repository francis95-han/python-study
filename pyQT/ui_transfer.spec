# -*- mode: python -*-

block_cipher = None


a = Analysis(['ui_transfer.py'],
             pathex=['D:\\Applications\\anaconda\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'D:\\Applications\\anaconda\\Lib\\site-packages\\PyQt5\\Qt\\plugins', 'D:\\code\\python\\python_study\\pyQT'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ui_transfer',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False )
