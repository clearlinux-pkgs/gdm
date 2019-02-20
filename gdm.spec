#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gdm
Version  : 3.30.2
Release  : 64
URL      : https://download.gnome.org/sources/gdm/3.30/gdm-3.30.2.tar.xz
Source0  : https://download.gnome.org/sources/gdm/3.30/gdm-3.30.2.tar.xz
Source1  : gdm-disable-a2dp-pulseaudio.service
Source2  : gdm.path
Source3  : gdm.tmpfiles
Summary  : Client Library for communicating with GDM daemon
Group    : Development/Tools
License  : GPL-2.0
Requires: gdm-bin = %{version}-%{release}
Requires: gdm-config = %{version}-%{release}
Requires: gdm-data = %{version}-%{release}
Requires: gdm-lib = %{version}-%{release}
Requires: gdm-libexec = %{version}-%{release}
Requires: gdm-license = %{version}-%{release}
Requires: gdm-locales = %{version}-%{release}
Requires: gdm-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-gnome
BuildRequires : dconf-dev
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : itstool
BuildRequires : keyutils-dev
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
Patch4: 0005-pulseaudio-to-ignore-A2DP.patch
Patch5: 0006-stateless-Scripting-Integration-Points.patch
Patch6: diet.patch
Patch7: CVE-2019-3825.patch

%description
GDM - GNOME Display Manager
===========================
http://wiki.gnome.org/Projects/GDM/

%package autostart
Summary: autostart components for the gdm package.
Group: Default

%description autostart
autostart components for the gdm package.


%package bin
Summary: bin components for the gdm package.
Group: Binaries
Requires: gdm-data = %{version}-%{release}
Requires: gdm-libexec = %{version}-%{release}
Requires: gdm-config = %{version}-%{release}
Requires: gdm-license = %{version}-%{release}
Requires: gdm-services = %{version}-%{release}

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
Requires: gdm-lib = %{version}-%{release}
Requires: gdm-bin = %{version}-%{release}
Requires: gdm-data = %{version}-%{release}
Provides: gdm-devel = %{version}-%{release}

%description dev
dev components for the gdm package.


%package lib
Summary: lib components for the gdm package.
Group: Libraries
Requires: gdm-data = %{version}-%{release}
Requires: gdm-libexec = %{version}-%{release}
Requires: gdm-license = %{version}-%{release}

%description lib
lib components for the gdm package.


%package libexec
Summary: libexec components for the gdm package.
Group: Default
Requires: gdm-config = %{version}-%{release}
Requires: gdm-license = %{version}-%{release}

%description libexec
libexec components for the gdm package.


%package license
Summary: license components for the gdm package.
Group: Default

%description license
license components for the gdm package.


%package locales
Summary: locales components for the gdm package.
Group: Default

%description locales
locales components for the gdm package.


%package services
Summary: services components for the gdm package.
Group: Systemd services

%description services
services components for the gdm package.


%prep
%setup -q -n gdm-3.30.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550698035
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%reconfigure --disable-static --enable-wayland-support=no \
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
export SOURCE_DATE_EPOCH=1550698035
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gdm
cp COPYING %{buildroot}/usr/share/package-licenses/gdm/COPYING
%make_install
%find_lang gdm
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/gdm-disable-a2dp-pulseaudio.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/gdm.path
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/tmpfiles.d/gdm.conf
## install_append content
mkdir -p %{buildroot}/usr/libexec
install -m 0755 ./gdm-disable-a2dp-pulseaudio.sh %{buildroot}/usr/libexec/gdm-disable-a2dp-pulseaudio.sh
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../gdm.path %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/gdm.path
ln -s ../gdm-disable-a2dp-pulseaudio.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/gdm-disable-a2dp-pulseaudio.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/gdm-disable-a2dp-pulseaudio.service
/usr/lib/systemd/system/multi-user.target.wants/gdm.path

%files bin
%defattr(-,root,root,-)
/usr/bin/gdm
/usr/bin/gdm-screenshot
/usr/bin/gdmflexiserver

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/udev/rules.d/61-gdm.rules
/usr/lib/tmpfiles.d/gdm.conf

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gdm-1.0.typelib
/usr/share/dbus-1/system.d/gdm.conf
/usr/share/dconf/profile/gdm
/usr/share/gdm/Init/Default
/usr/share/gdm/PostLogin/Default
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

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gdm-disable-a2dp-pulseaudio.sh
/usr/libexec/gdm-disable-wayland
/usr/libexec/gdm-host-chooser
/usr/libexec/gdm-session-worker
/usr/libexec/gdm-simple-chooser
/usr/libexec/gdm-wayland-session
/usr/libexec/gdm-x-session

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gdm/COPYING

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/gdm-disable-a2dp-pulseaudio.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/gdm.path
/usr/lib/systemd/system/gdm-disable-a2dp-pulseaudio.service
/usr/lib/systemd/system/gdm.path
/usr/lib/systemd/system/gdm.service

%files locales -f gdm.lang
%defattr(-,root,root,-)

