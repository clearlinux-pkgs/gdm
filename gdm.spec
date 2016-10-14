#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gdm
Version  : 3.22.1
Release  : 2
URL      : https://download.gnome.org/sources/gdm/3.22/gdm-3.22.1.tar.xz
Source0  : https://download.gnome.org/sources/gdm/3.22/gdm-3.22.1.tar.xz
Summary  : Client Library for communicating with GDM daemon
Group    : Development/Tools
License  : GPL-2.0
Requires: gdm-bin
Requires: gdm-config
Requires: gdm-lib
Requires: gdm-data
Requires: gdm-locales
BuildRequires : Linux-PAM-dev
BuildRequires : dconf-dev
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libXinerama-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-python
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(accountsservice)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xau)
BuildRequires : systemd-dev

%description
GDM - GNOME Display Manager
http://wiki.gnome.org/Projects/GDM/
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

%package bin
Summary: bin components for the gdm package.
Group: Binaries
Requires: gdm-data
Requires: gdm-config

%description bin
bin components for the gdm package.


%package config
Summary: config components for the gdm package.
Group: Default

%description config
config components for the gdm package.


%package data
Summary: data components for the gdm package.
Group: Data

%description data
data components for the gdm package.


%package dev
Summary: dev components for the gdm package.
Group: Development
Requires: gdm-lib
Requires: gdm-bin
Requires: gdm-data
Provides: gdm-devel

%description dev
dev components for the gdm package.


%package lib
Summary: lib components for the gdm package.
Group: Libraries
Requires: gdm-data
Requires: gdm-config

%description lib
lib components for the gdm package.


%package locales
Summary: locales components for the gdm package.
Group: Default

%description locales
locales components for the gdm package.


%prep
%setup -q -n gdm-3.22.1

%build
export LANG=C
%configure --disable-static --enable-wayland-support \
--enable-ipv6 \
--disable-schemas-compile \
--with-initial-vt=7 \
--without-plymouth
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang gdm

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gdm
/usr/bin/gdm-screenshot
/usr/bin/gdmflexiserver
/usr/libexec/gdm-host-chooser
/usr/libexec/gdm-session-worker
/usr/libexec/gdm-simple-chooser
/usr/libexec/gdm-wayland-session
/usr/libexec/gdm-x-session

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/gdm.service

%files data
%defattr(-,root,root,-)
/usr/share/dconf/profile/gdm
/usr/share/gdm/gdb-cmd
/usr/share/gdm/gdm.schemas
/usr/share/gdm/greeter-dconf-defaults
/usr/share/gdm/greeter/applications/mime-dummy-handler.desktop
/usr/share/gdm/greeter/applications/mimeapps.list
/usr/share/gdm/greeter/autostart/orca-autostart.desktop
/usr/share/gdm/locale.alias
/usr/share/glib-2.0/schemas/org.gnome.login-screen.gschema.xml
/usr/share/help/C/gdm/index.docbook
/usr/share/help/C/gdm/legal.xml
/usr/share/help/ca/gdm/index.docbook
/usr/share/help/ca/gdm/legal.xml
/usr/share/help/cs/gdm/index.docbook
/usr/share/help/cs/gdm/legal.xml
/usr/share/help/de/gdm/index.docbook
/usr/share/help/de/gdm/legal.xml
/usr/share/help/el/gdm/index.docbook
/usr/share/help/el/gdm/legal.xml
/usr/share/help/en_GB/gdm/index.docbook
/usr/share/help/en_GB/gdm/legal.xml
/usr/share/help/es/gdm/index.docbook
/usr/share/help/es/gdm/legal.xml
/usr/share/help/fr/gdm/index.docbook
/usr/share/help/fr/gdm/legal.xml
/usr/share/help/gl/gdm/index.docbook
/usr/share/help/gl/gdm/legal.xml
/usr/share/help/hu/gdm/index.docbook
/usr/share/help/hu/gdm/legal.xml
/usr/share/help/id/gdm/index.docbook
/usr/share/help/id/gdm/legal.xml
/usr/share/help/it/gdm/index.docbook
/usr/share/help/it/gdm/legal.xml
/usr/share/help/ko/gdm/index.docbook
/usr/share/help/ko/gdm/legal.xml
/usr/share/help/oc/gdm/index.docbook
/usr/share/help/oc/gdm/legal.xml
/usr/share/help/pt_BR/gdm/index.docbook
/usr/share/help/pt_BR/gdm/legal.xml
/usr/share/help/ro/gdm/index.docbook
/usr/share/help/ro/gdm/legal.xml
/usr/share/help/ru/gdm/index.docbook
/usr/share/help/ru/gdm/legal.xml
/usr/share/help/sl/gdm/index.docbook
/usr/share/help/sl/gdm/legal.xml
/usr/share/help/sv/gdm/index.docbook
/usr/share/help/sv/gdm/legal.xml
/usr/share/help/te/gdm/index.docbook
/usr/share/help/te/gdm/legal.xml
/usr/share/help/tr/gdm/index.docbook
/usr/share/help/tr/gdm/legal.xml
/usr/share/help/uk/gdm/index.docbook
/usr/share/help/uk/gdm/legal.xml
/usr/share/help/zh_CN/gdm/index.docbook
/usr/share/help/zh_CN/gdm/legal.xml
/usr/share/icons/hicolor/16x16/apps/gdm-xnest.png
/usr/share/icons/hicolor/32x32/apps/gdm-setup.png
/usr/share/icons/hicolor/32x32/apps/gdm-xnest.png
/usr/share/pixmaps/gdm-foot-logo.png
/usr/share/pixmaps/gdm-setup.png
/usr/share/pixmaps/gdm-xnest.png
/usr/share/pixmaps/gdm.png
/usr/share/pixmaps/nobody.png
/usr/share/pixmaps/nohost.png

%files dev
%defattr(-,root,root,-)
/usr/include/gdm/gdm-client-glue.h
/usr/include/gdm/gdm-client.h
/usr/include/gdm/gdm-sessions.h
/usr/include/gdm/gdm-user-switching.h
/usr/lib64/*.so
/usr/lib64/girepository-1.0/Gdm-1.0.typelib
/usr/lib64/pkgconfig/*.pc
/usr/share/gir-1.0/*.gir

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/security/pam_gdm.so

%files locales -f gdm.lang 
%defattr(-,root,root,-)

