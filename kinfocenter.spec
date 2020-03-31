#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kinfocenter
Version  : 5.18.4.1
Release  : 37
URL      : https://download.kde.org/stable/plasma/5.18.4/kinfocenter-5.18.4.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.18.4/kinfocenter-5.18.4.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.18.4/kinfocenter-5.18.4.1.tar.xz.sig
Summary  : A utility that provides information about a computer system
Group    : Development/Tools
License  : GPL-3.0
Requires: kinfocenter-bin = %{version}-%{release}
Requires: kinfocenter-data = %{version}-%{release}
Requires: kinfocenter-lib = %{version}-%{release}
Requires: kinfocenter-license = %{version}-%{release}
Requires: kinfocenter-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : mesa-dev
BuildRequires : pciutils-dev
BuildRequires : qtbase-dev mesa-dev

%description
this kcontrol module shows the current configuration of the IEEE 1394 bus.
It uses libraw1394 (see www.linux1394.org). I don't know how the 1394 apis
on other OS's look, feel free to port it :-)

%package bin
Summary: bin components for the kinfocenter package.
Group: Binaries
Requires: kinfocenter-data = %{version}-%{release}
Requires: kinfocenter-license = %{version}-%{release}

%description bin
bin components for the kinfocenter package.


%package data
Summary: data components for the kinfocenter package.
Group: Data

%description data
data components for the kinfocenter package.


%package doc
Summary: doc components for the kinfocenter package.
Group: Documentation

%description doc
doc components for the kinfocenter package.


%package lib
Summary: lib components for the kinfocenter package.
Group: Libraries
Requires: kinfocenter-data = %{version}-%{release}
Requires: kinfocenter-license = %{version}-%{release}

%description lib
lib components for the kinfocenter package.


%package license
Summary: license components for the kinfocenter package.
Group: Default

%description license
license components for the kinfocenter package.


%package locales
Summary: locales components for the kinfocenter package.
Group: Default

%description locales
locales components for the kinfocenter package.


%prep
%setup -q -n kinfocenter-5.18.4.1
cd %{_builddir}/kinfocenter-5.18.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585676905
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1585676905
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kinfocenter
cp %{_builddir}/kinfocenter-5.18.4.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kinfocenter/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kinfocenter-5.18.4.1/Modules/about-distro/COPYING %{buildroot}/usr/share/package-licenses/kinfocenter/842745cb706f8f2126506f544492f7a80dbe29b3
pushd clr-build
%make_install
popd
%find_lang kcminfo
%find_lang kcmsamba
%find_lang kcmusb
%find_lang kcmview1394
%find_lang kinfocenter
%find_lang kcm-about-distro
%find_lang kcm_energyinfo
%find_lang kcm_fileindexermonitor
%find_lang kcm_memory
%find_lang kcm_pci
%find_lang kcmdevinfo
%find_lang kcmnic
%find_lang kcmopengl
## install_append content
mv %{buildroot}/etc/xdg/* %{buildroot}/usr/share/xdg/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kinfocenter

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kinfocenter.desktop
/usr/share/desktop-directories/kinfocenter.directory
/usr/share/kcmusb/usb.ids
/usr/share/kpackage/kcms/kcm_energyinfo/contents/ui/Graph.qml
/usr/share/kpackage/kcms/kcm_energyinfo/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_energyinfo/metadata.desktop
/usr/share/kpackage/kcms/kcm_energyinfo/metadata.json
/usr/share/kpackage/kcms/kcm_fileindexermonitor/contents/ui/constants.js
/usr/share/kpackage/kcms/kcm_fileindexermonitor/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_fileindexermonitor/metadata.desktop
/usr/share/kpackage/kcms/kcm_fileindexermonitor/metadata.json
/usr/share/kservices5/about-distro.desktop
/usr/share/kservices5/deviceinfocategory.desktop
/usr/share/kservices5/devinfo.desktop
/usr/share/kservices5/dma.desktop
/usr/share/kservices5/graphicalinfocategory.desktop
/usr/share/kservices5/interrupts.desktop
/usr/share/kservices5/ioports.desktop
/usr/share/kservices5/kcm_energyinfo.desktop
/usr/share/kservices5/kcm_fileindexermonitor.desktop
/usr/share/kservices5/kcm_memory.desktop
/usr/share/kservices5/kcm_pci.desktop
/usr/share/kservices5/kcmusb.desktop
/usr/share/kservices5/lostfoundcategory.desktop
/usr/share/kservices5/networkinfocategory.desktop
/usr/share/kservices5/nic.desktop
/usr/share/kservices5/smbstatus.desktop
/usr/share/kservices5/wayland.desktop
/usr/share/kservices5/xserver.desktop
/usr/share/kservicetypes5/kinfocentercategory.desktop
/usr/share/kxmlgui5/kinfocenter/kinfocenterui.rc
/usr/share/metainfo/org.kde.kinfocenter.appdata.xml
/usr/share/xdg/kinfocenter.menu

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/ca/kinfocenter/index.docbook
/usr/share/doc/HTML/ca/kinfocenter/kinfocenter.png
/usr/share/doc/HTML/de/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/de/kinfocenter/index.docbook
/usr/share/doc/HTML/en/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/en/kinfocenter/index.docbook
/usr/share/doc/HTML/en/kinfocenter/kinfocenter.png
/usr/share/doc/HTML/id/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/id/kinfocenter/index.docbook
/usr/share/doc/HTML/it/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/it/kinfocenter/index.docbook
/usr/share/doc/HTML/nl/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/nl/kinfocenter/index.docbook
/usr/share/doc/HTML/pt/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/pt/kinfocenter/index.docbook
/usr/share/doc/HTML/pt_BR/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kinfocenter/index.docbook
/usr/share/doc/HTML/pt_BR/kinfocenter/kinfocenter.png
/usr/share/doc/HTML/ru/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/ru/kinfocenter/index.docbook
/usr/share/doc/HTML/sr/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/sr/kinfocenter/index.docbook
/usr/share/doc/HTML/sr@latin/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kinfocenter/index.docbook
/usr/share/doc/HTML/sv/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/sv/kinfocenter/index.docbook
/usr/share/doc/HTML/uk/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/uk/kinfocenter/index.docbook
/usr/share/doc/HTML/uk/kinfocenter/kinfocenter.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_about_distro.so
/usr/lib64/qt5/plugins/kcm_devinfo.so
/usr/lib64/qt5/plugins/kcm_info.so
/usr/lib64/qt5/plugins/kcm_memory.so
/usr/lib64/qt5/plugins/kcm_nic.so
/usr/lib64/qt5/plugins/kcm_pci.so
/usr/lib64/qt5/plugins/kcm_samba.so
/usr/lib64/qt5/plugins/kcm_usb.so
/usr/lib64/qt5/plugins/kcms/kcm_energyinfo.so
/usr/lib64/qt5/plugins/kcms/kcm_fileindexermonitor.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kinfocenter/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kinfocenter/842745cb706f8f2126506f544492f7a80dbe29b3

%files locales -f kcminfo.lang -f kcmsamba.lang -f kcmusb.lang -f kcmview1394.lang -f kinfocenter.lang -f kcm-about-distro.lang -f kcm_energyinfo.lang -f kcm_fileindexermonitor.lang -f kcm_memory.lang -f kcm_pci.lang -f kcmdevinfo.lang -f kcmnic.lang -f kcmopengl.lang
%defattr(-,root,root,-)

