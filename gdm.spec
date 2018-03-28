#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gdm
Version  : 3.28.0
Release  : 35
URL      : https://download.gnome.org/sources/gdm/3.28/gdm-3.28.0.tar.xz
Source0  : https://download.gnome.org/sources/gdm/3.28/gdm-3.28.0.tar.xz
Source1  : gdm-hw-accel.service
Source2  : gdm.tmpfiles
Summary  : Client Library for communicating with GDM daemon
Group    : Development/Tools
License  : GPL-2.0
Requires: gdm-bin
Requires: gdm-config
Requires: gdm-data
Requires: gdm-lib
Requires: gdm-locales
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : dconf-dev
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : gobject-introspection-dev
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libXinerama-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxml2-dev
BuildRequires : m4
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config-dev
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
BuildRequires : pkgconfig(xcb)
BuildRequires : systemd-dev
Patch1: 0001-data-Integrate-with-the-Clear-Linux-PAM-configuratio.patch
Patch2: 0002-Use-stateless-gdmconfdir-for-integration-into-Clear-.patch
Patch3: 0003-pam-Allow-gnome-initial-setup-to-operate-in-gdm-laun.patch
Patch4: 0004-conflict-with-gdm-hw-accel.service.patch

%description
GDM - GNOME Display Manager
http://wiki.gnome.org/Projects/GDM/
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

%package autostart
Summary: autostart components for the gdm package.
Group: Default

%description autostart
autostart components for the gdm package.


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

%description lib
lib components for the gdm package.


%package locales
Summary: locales components for the gdm package.
Group: Default

%description locales
locales components for the gdm package.


%prep
%setup -q -n gdm-3.28.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522205318
%reconfigure --disable-static --enable-wayland-support=yes \
--enable-ipv6 \
--disable-schemas-compile \
--with-initial-vt=7 \
--without-plymouth \
--with-pam-prefix=/usr/share \
--with-default-pam-config=lfs \
--with-dbus-sys=/usr/share/dbus-1/system.d \
--with-custom-conf=/etc/gdm/custom.conf \
--enable-gdm-xsession
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522205318
rm -rf %{buildroot}
%make_install
%find_lang gdm
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/gdm-hw-accel.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/gdm.conf
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../gdm-hw-accel.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/gdm-hw-accel.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/gdm-hw-accel.service

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
%exclude /usr/lib/systemd/system/multi-user.target.wants/gdm-hw-accel.service
/usr/lib/systemd/system/gdm-hw-accel.service
/usr/lib/systemd/system/gdm.service
/usr/lib/tmpfiles.d/gdm.conf
/usr/lib/udev/rules.d/61-gdm.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gdm-1.0.typelib
/usr/share/dbus-1/system.d/gdm.conf
/usr/share/dconf/profile/gdm
/usr/share/gdm/Init/Default
/usr/share/gdm/PostLogin/Default.sample
/usr/share/gdm/PostSession/Default
/usr/share/gdm/PreSession/Default
/usr/share/gdm/Xsession
/usr/share/gdm/gdb-cmd
/usr/share/gdm/gdm.schemas
/usr/share/gdm/greeter-dconf-defaults
/usr/share/gdm/greeter/applications/mime-dummy-handler.desktop
/usr/share/gdm/greeter/applications/mimeapps.list
/usr/share/gdm/greeter/autostart/orca-autostart.desktop
/usr/share/gdm/locale.alias
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.login-screen.gschema.xml
/usr/share/gnome-session/sessions/gnome-login.session
/usr/share/icons/hicolor/16x16/apps/gdm-xnest.png
/usr/share/icons/hicolor/32x32/apps/gdm-setup.png
/usr/share/icons/hicolor/32x32/apps/gdm-xnest.png
/usr/share/pam.d/gdm-autologin
/usr/share/pam.d/gdm-fingerprint
/usr/share/pam.d/gdm-launch-environment
/usr/share/pam.d/gdm-password
/usr/share/pam.d/gdm-pin
/usr/share/pam.d/gdm-smartcard
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
/usr/include/gdm/gdm-pam-extensions.h
/usr/include/gdm/gdm-sessions.h
/usr/include/gdm/gdm-user-switching.h
/usr/lib64/libgdm.so
/usr/lib64/pkgconfig/gdm-pam-extensions.pc
/usr/lib64/pkgconfig/gdm.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdm.so.1
/usr/lib64/libgdm.so.1.0.0
/usr/lib64/security/pam_gdm.so

%files locales -f gdm.lang
%defattr(-,root,root,-)

