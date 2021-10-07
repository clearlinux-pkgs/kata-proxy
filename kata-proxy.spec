#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kata-proxy
Version  : 1.10.8
Release  : 36
URL      : https://github.com/kata-containers/proxy/archive/1.10.8/proxy-1.10.8.tar.gz
Source0  : https://github.com/kata-containers/proxy/archive/1.10.8/proxy-1.10.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT MPL-2.0-no-copyleft-exception
Requires: kata-proxy-libexec = %{version}-%{release}
Requires: kata-proxy-license = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-add-fake-autogen.patch

%description
[![Build Status](https://travis-ci.org/kata-containers/proxy.svg?branch=master)](https://travis-ci.org/kata-containers/proxy)
[![codecov](https://codecov.io/gh/kata-containers/proxy/branch/master/graph/badge.svg)](https://codecov.io/gh/kata-containers/proxy)

%package libexec
Summary: libexec components for the kata-proxy package.
Group: Default
Requires: kata-proxy-license = %{version}-%{release}

%description libexec
libexec components for the kata-proxy package.


%package license
Summary: license components for the kata-proxy package.
Group: Default

%description license
license components for the kata-proxy package.


%prep
%setup -q -n proxy-1.10.8
cd %{_builddir}/proxy-1.10.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624661609
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static ;export GOPATH="${PWD}/gopath/" \
;mkdir -p "${GOPATH}/src/github.com/kata-containers/" \
;ln -sf "${PWD}" "${GOPATH}/src/github.com/kata-containers/proxy" \
;cd "${GOPATH}/src/github.com/kata-containers/proxy"
## make_prepend content
export GO111MODULE="auto"
## make_prepend end
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1624661609
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kata-proxy
cp %{_builddir}/proxy-1.10.8/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/proxy-1.10.8/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/0e9ad2a801d95231296b0b613db53147258260b1
cp %{_builddir}/proxy-1.10.8/vendor/github.com/hashicorp/yamux/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/784701375491309231e6d26850c410e36c246d15
cp %{_builddir}/proxy-1.10.8/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/proxy-1.10.8/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/proxy-1.10.8/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/5e630aeef4ff3e9b29a46622496b3fbbf5d7fe56
cp %{_builddir}/proxy-1.10.8/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/proxy-1.10.8/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/d6a5f1ecaedd723c325a2063375b3517e808a2b5
%make_install

%files
%defattr(-,root,root,-)

%files libexec
%defattr(-,root,root,-)
/usr/libexec/kata-containers/kata-proxy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kata-proxy/0e9ad2a801d95231296b0b613db53147258260b1
/usr/share/package-licenses/kata-proxy/5e630aeef4ff3e9b29a46622496b3fbbf5d7fe56
/usr/share/package-licenses/kata-proxy/784701375491309231e6d26850c410e36c246d15
/usr/share/package-licenses/kata-proxy/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/kata-proxy/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/kata-proxy/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/kata-proxy/d6a5f1ecaedd723c325a2063375b3517e808a2b5
