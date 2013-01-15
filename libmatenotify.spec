#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc

Summary:	Libraries for mate notify
Name:		libmatenotify
Version:	1.5.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	28a1526c93f9a28a3cea9fdefbc47b41
URL:		http://wiki.mate-desktop.org/libmatenotify
BuildRequires:	dbus-devel >= 0.76
BuildRequires:	dbus-glib-devel >= 0.76
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk+2-devel >= 2:2.18
BuildRequires:	mate-common
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries for mate notify.

%package devel
Summary:	Development libraries for libmatenotify
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development libraries for libmatenotify

%package apidocs
Summary:	libmatenotify API documentation
Summary(hu.UTF-8):	libmatenotify API dokumentáció
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmatenotify
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libmatenotify API documentation.

%description apidocs -l hu.UTF-8
libmatenotify API dokumentáció.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmatenotify.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--disable-static

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:%{__rm} -rf $RPM_BUILD_ROOT%{_gtkdocdir}/%{name}}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/mate-notify-send
%attr(755,root,root) %{_libdir}/libmatenotify.so.*.*.*
%ghost %{_libdir}/libmatenotify.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmatenotify.so
%{_pkgconfigdir}/libmatenotify.pc
%{_includedir}/libmatenotify

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif
