#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gdm
Version  : 44.1
Release  : 104
URL      : https://download.gnome.org/sources/gdm/44/gdm-44.1.tar.xz
Source0  : https://download.gnome.org/sources/gdm/44/gdm-44.1.tar.xz
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
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dconf-dev
BuildRequires : gobject-introspection-dev
BuildRequires : itstool
BuildRequires : keyutils-dev
BuildRequires : libXinerama-dev
BuildRequires : libcanberra-dev
BuildRequires : libxml2-dev
BuildRequires : pkgconfig(accountsservice)
BuildRequires : pkgconfig(audit)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : systemd-dev
BuildRequires : xorg-server
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-data-Integrate-with-the-Clear-Linux-PAM-configuratio.patch
Patch2: 0002-Use-stateless-gdmconfdir-for-integration-into-Clear-.patch
Patch3: 0003-pam-Allow-gnome-initial-setup-to-operate-in-gdm-laun.patch
Patch4: 0004-pulseaudio-to-ignore-A2DP.patch
Patch5: 0005-stateless-Scripting-Integration-Points.patch
Patch6: 0006-gdm3.service-wait-for-drm-device-before-trying-to-st.patch

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
Requires: gdm = %{version}-%{release}

%description dev
dev components for the gdm package.


%package doc
Summary: doc components for the gdm package.
Group: Documentation

%description doc
doc components for the gdm package.


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
Requires: systemd

%description services
services components for the gdm package.


%prep
%setup -q -n gdm-44.1
cd %{_builddir}/gdm-44.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
pushd ..
cp -a gdm-44.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685507409
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dwayland-support=true \
-Dipv6=true \
-Dplymouth=disabled \
-Dpam-prefix=/usr/share \
-Ddefault-pam-config=lfs \
-Ddbus-sys=/usr/share/dbus-1/system.d \
-Dcustom-conf=/etc/gdm/custom.conf \
-Dgdm-xsession=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dwayland-support=true \
-Dipv6=true \
-Dplymouth=disabled \
-Dpam-prefix=/usr/share \
-Ddefault-pam-config=lfs \
-Ddbus-sys=/usr/share/dbus-1/system.d \
-Dcustom-conf=/etc/gdm/custom.conf \
-Dgdm-xsession=true  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gdm
cp %{_builddir}/gdm-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gdm/4cc77b90af91e615a64ae04893fdffa7939db84c || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gdm
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/gdm-disable-a2dp-pulseaudio.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/gdm.path
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/tmpfiles.d/gdm.conf
## install_append content
mkdir -p %{buildroot}/usr/libexec
install -m 0755 ./gdm-disable-a2dp-pulseaudio.sh %{buildroot}/usr/libexec/gdm-disable-a2dp-pulseaudio.sh

mkdir -p %{buildroot}/usr/lib/systemd/system/graphical.target.wants/
ln -s ../gdm.path %{buildroot}/usr/lib/systemd/system/graphical.target.wants/gdm.path
ln -s ../gdm-disable-a2dp-pulseaudio.service %{buildroot}/usr/lib/systemd/system/graphical.target.wants/gdm-disable-a2dp-pulseaudio.service
mv %{buildroot}/usr/sbin/* %{buildroot}/usr/bin/
mkdir -p %{buildroot}/V3/usr/bin/
mv %{buildroot}-v3/usr/sbin/* %{buildroot}/V3/usr/bin/ || :
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/graphical.target.wants/gdm-disable-a2dp-pulseaudio.service
/usr/lib/systemd/system/graphical.target.wants/gdm.path

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gdm
/V3/usr/bin/gdm-screenshot
/V3/usr/bin/gdmflexiserver
/usr/bin/gdm
/usr/bin/gdm-screenshot
/usr/bin/gdmflexiserver

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/gdm.conf
/usr/lib/udev/rules.d/61-gdm.rules

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
/usr/share/pam.d/gdm-autologin
/usr/share/pam.d/gdm-fingerprint
/usr/share/pam.d/gdm-launch-environment
/usr/share/pam.d/gdm-password
/usr/share/pam.d/gdm-smartcard

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

%files doc
%defattr(0644,root,root,0755)
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
/usr/share/help/eu/gdm/index.docbook
/usr/share/help/eu/gdm/legal.xml
/usr/share/help/fr/gdm/index.docbook
/usr/share/help/fr/gdm/legal.xml
/usr/share/help/gl/gdm/index.docbook
/usr/share/help/gl/gdm/legal.xml
/usr/share/help/hr/gdm/index.docbook
/usr/share/help/hr/gdm/legal.xml
/usr/share/help/hu/gdm/index.docbook
/usr/share/help/hu/gdm/legal.xml
/usr/share/help/id/gdm/index.docbook
/usr/share/help/id/gdm/legal.xml
/usr/share/help/it/gdm/index.docbook
/usr/share/help/it/gdm/legal.xml
/usr/share/help/ka/gdm/index.docbook
/usr/share/help/ka/gdm/legal.xml
/usr/share/help/ko/gdm/index.docbook
/usr/share/help/ko/gdm/legal.xml
/usr/share/help/nl/gdm/index.docbook
/usr/share/help/nl/gdm/legal.xml
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

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgdm.so.1.0.0
/V3/usr/lib64/security/pam_gdm.so
/usr/lib64/libgdm.so.1
/usr/lib64/libgdm.so.1.0.0
/usr/lib64/security/pam_gdm.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gdm-host-chooser
/V3/usr/libexec/gdm-runtime-config
/V3/usr/libexec/gdm-session-worker
/V3/usr/libexec/gdm-simple-chooser
/V3/usr/libexec/gdm-wait-for-drm
/V3/usr/libexec/gdm-wayland-session
/V3/usr/libexec/gdm-x-session
/usr/libexec/gdm-disable-a2dp-pulseaudio.sh
/usr/libexec/gdm-host-chooser
/usr/libexec/gdm-runtime-config
/usr/libexec/gdm-session-worker
/usr/libexec/gdm-simple-chooser
/usr/libexec/gdm-wait-for-drm
/usr/libexec/gdm-wayland-session
/usr/libexec/gdm-x-session

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gdm/4cc77b90af91e615a64ae04893fdffa7939db84c

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/graphical.target.wants/gdm-disable-a2dp-pulseaudio.service
%exclude /usr/lib/systemd/system/graphical.target.wants/gdm.path
/usr/lib/systemd/system/gdm-disable-a2dp-pulseaudio.service
/usr/lib/systemd/system/gdm.path
/usr/lib/systemd/system/gdm.service
/usr/lib/systemd/user/gnome-session@gnome-login.target.d/session.conf

%files locales -f gdm.lang
%defattr(-,root,root,-)

