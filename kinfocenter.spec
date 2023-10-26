#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: 250a666
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kinfocenter
Version  : 5.27.9
Release  : 91
URL      : https://download.kde.org/stable/plasma/5.27.9/kinfocenter-5.27.9.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.9/kinfocenter-5.27.9.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.9/kinfocenter-5.27.9.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 FSFAP GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: kinfocenter-bin = %{version}-%{release}
Requires: kinfocenter-data = %{version}-%{release}
Requires: kinfocenter-lib = %{version}-%{release}
Requires: kinfocenter-license = %{version}-%{release}
Requires: kinfocenter-locales = %{version}-%{release}
Requires: systemsettings
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : pciutils-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libusb-1.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: CC0-1.0
-->
See example/*.
Essentially you place an rc file in the file system that defines the distro logo
and website url. The file ought to be in some XDG_CONFIG_DIRS dir.

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


%package dev
Summary: dev components for the kinfocenter package.
Group: Development
Requires: kinfocenter-lib = %{version}-%{release}
Requires: kinfocenter-bin = %{version}-%{release}
Requires: kinfocenter-data = %{version}-%{release}
Provides: kinfocenter-devel = %{version}-%{release}
Requires: kinfocenter = %{version}-%{release}

%description dev
dev components for the kinfocenter package.


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
%setup -q -n kinfocenter-5.27.9
cd %{_builddir}/kinfocenter-5.27.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698281191
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1698281191
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kinfocenter
cp %{_builddir}/kinfocenter-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kinfocenter/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kinfocenter/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kinfocenter/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/FSFAP.txt %{buildroot}/usr/share/package-licenses/kinfocenter/da20b47077b3106fb65720d6fef309f39043fa60 || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kinfocenter/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kinfocenter/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kinfocenter/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kinfocenter/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kinfocenter/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kinfocenter/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kinfocenter/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kinfocenter/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kinfocenter-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kinfocenter/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kinfocenter-%{version}/Modules/firmware_security/kcm_firmware_security.json.license %{buildroot}/usr/share/package-licenses/kinfocenter/f9bb2e988a5b97ddfe98979cd3c3021017f5cbfd || :
cp %{_builddir}/kinfocenter-%{version}/logo.png.license %{buildroot}/usr/share/package-licenses/kinfocenter/2fc0cc7725ba1907f2d31a14c4c705e64a49e76e || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kcmsamba
%find_lang kcmusb
%find_lang kcm_about-distro
%find_lang kcm_cpu
%find_lang kcm_egl
%find_lang kcm_energyinfo
%find_lang kcm_firmware_security
%find_lang kcm_glx
%find_lang kcm_interrupts
%find_lang kcm_kwinsupportinfo
%find_lang kcm_nic
%find_lang kcm_opencl
%find_lang kcm_pci
%find_lang kcm_vulkan
%find_lang kcm_wayland
%find_lang kcm_xserver
%find_lang kcmdevinfo
## install_append content
mv %{buildroot}/etc/xdg/* %{buildroot}/usr/share/xdg/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kauth/kinfocenter-dmidecode-helper
/usr/lib64/libexec/kauth/kinfocenter-dmidecode-helper

%files bin
%defattr(-,root,root,-)
/usr/bin/kinfocenter

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_about-distro.desktop
/usr/share/applications/org.kde.kinfocenter.desktop
/usr/share/dbus-1/system-services/org.kde.kinfocenter.dmidecode.service
/usr/share/dbus-1/system.d/org.kde.kinfocenter.dmidecode.conf
/usr/share/desktop-directories/kinfocenter.directory
/usr/share/kinfocenter/categories/basicinformation.desktop
/usr/share/kinfocenter/categories/detailedinformation.desktop
/usr/share/kinfocenter/categories/deviceinfocategory.desktop
/usr/share/kinfocenter/categories/graphicalinfocategory.desktop
/usr/share/kinfocenter/categories/lostfoundcategory.desktop
/usr/share/kinfocenter/categories/networkinfocategory.desktop
/usr/share/kpackage/kcms/kcm_about-distro/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_cpu/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_egl/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_energyinfo/contents/ui/Graph.qml
/usr/share/kpackage/kcms/kcm_energyinfo/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_firmware_security/contents/code/fwupdmgr.sh
/usr/share/kpackage/kcms/kcm_firmware_security/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_glx/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_interrupts/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_kwinsupportinfo/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_nic/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_opencl/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_pci/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_vulkan/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_wayland/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_xserver/contents/ui/main.qml
/usr/share/kpackage/kcms/kcmsamba/contents/ui/ShareListItem.qml
/usr/share/kpackage/kcms/kcmsamba/contents/ui/main.qml
/usr/share/metainfo/org.kde.kinfocenter.appdata.xml
/usr/share/polkit-1/actions/org.kde.kinfocenter.dmidecode.policy
/usr/share/xdg/kinfocenter.menu

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libKInfoCenterInternal.so
/usr/lib64/libKInfoCenterInternal.so

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
/usr/share/doc/HTML/es/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/es/kinfocenter/index.docbook
/usr/share/doc/HTML/fr/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/fr/kinfocenter/index.docbook
/usr/share/doc/HTML/id/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/id/kinfocenter/index.docbook
/usr/share/doc/HTML/it/kinfocenter/index.cache.bz2
/usr/share/doc/HTML/it/kinfocenter/index.docbook
/usr/share/doc/HTML/it/kinfocenter/kinfocenter.png
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
/V3/usr/lib64/qt5/plugins/plasma/kcms/kcm_about-distro.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kcm_energyinfo.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_cpu.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_devinfo.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_egl.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_firmware_security.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_glx.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_interrupts.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_kwinsupportinfo.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_nic.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_opencl.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_pci.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_samba.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_usb.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_vulkan.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_wayland.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_xserver.so
/usr/lib64/qt5/plugins/plasma/kcms/kcm_about-distro.so
/usr/lib64/qt5/plugins/plasma/kcms/kcm_energyinfo.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_cpu.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_devinfo.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_egl.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_firmware_security.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_glx.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_interrupts.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_kwinsupportinfo.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_nic.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_opencl.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_pci.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_samba.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_usb.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_vulkan.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_wayland.so
/usr/lib64/qt5/plugins/plasma/kcms/kinfocenter/kcm_xserver.so
/usr/lib64/qt5/qml/org/kde/kinfocenter/private/CommandOutputKCM.qml
/usr/lib64/qt5/qml/org/kde/kinfocenter/private/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kinfocenter/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kinfocenter/2fc0cc7725ba1907f2d31a14c4c705e64a49e76e
/usr/share/package-licenses/kinfocenter/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
/usr/share/package-licenses/kinfocenter/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kinfocenter/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kinfocenter/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kinfocenter/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kinfocenter/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kinfocenter/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kinfocenter/da20b47077b3106fb65720d6fef309f39043fa60
/usr/share/package-licenses/kinfocenter/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kinfocenter/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/kinfocenter/f9bb2e988a5b97ddfe98979cd3c3021017f5cbfd

%files locales -f kcmsamba.lang -f kcmusb.lang -f kcm_about-distro.lang -f kcm_cpu.lang -f kcm_egl.lang -f kcm_energyinfo.lang -f kcm_firmware_security.lang -f kcm_glx.lang -f kcm_interrupts.lang -f kcm_kwinsupportinfo.lang -f kcm_nic.lang -f kcm_opencl.lang -f kcm_pci.lang -f kcm_vulkan.lang -f kcm_wayland.lang -f kcm_xserver.lang -f kcmdevinfo.lang
%defattr(-,root,root,-)

