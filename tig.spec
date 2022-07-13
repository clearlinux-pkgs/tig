#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tig
Version  : 2.5.6
Release  : 19
URL      : https://github.com/jonas/tig/releases/download/tig-2.5.6/tig-2.5.6.tar.gz
Source0  : https://github.com/jonas/tig/releases/download/tig-2.5.6/tig-2.5.6.tar.gz
Summary  : Tig: text-mode interface for git
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: tig-bin = %{version}-%{release}
Requires: tig-license = %{version}-%{release}
Requires: tig-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(ncurses)
BuildRequires : readline-dev

%description
Tig is a git repository browser that additionally can act as a pager
for output from various git commands.

When browsing repositories, it uses the underlying git commands to
present the user with various views, such as summarized revision log
and showing the commit with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.

%package bin
Summary: bin components for the tig package.
Group: Binaries
Requires: tig-license = %{version}-%{release}

%description bin
bin components for the tig package.


%package license
Summary: license components for the tig package.
Group: Default

%description license
license components for the tig package.


%package man
Summary: man components for the tig package.
Group: Default

%description man
man components for the tig package.


%prep
%setup -q -n tig-2.5.6
cd %{_builddir}/tig-2.5.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657729109
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}  all doc-man

%install
export SOURCE_DATE_EPOCH=1657729109
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tig
cp %{_builddir}/tig-2.5.6/COPYING %{buildroot}/usr/share/package-licenses/tig/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install install-doc-man

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tig

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tig/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tig.1
/usr/share/man/man5/tigrc.5
/usr/share/man/man7/tigmanual.7
