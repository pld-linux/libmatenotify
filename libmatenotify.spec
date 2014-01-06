# NOTE: deprecated package, MATE 1.6 uses libnotify 0.7+
#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc

Summary:	MATE Notifications library
Summary(pl.UTF-8):	Biblioteka powiadomień dla środowiska MATE
Name:		libmatenotify
Version:	1.5.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	28a1526c93f9a28a3cea9fdefbc47b41
URL:		http://wiki.mate-desktop.org/libmatenotify
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.10
BuildRequires:	dbus-devel >= 0.76
BuildRequires:	dbus-glib-devel >= 0.76
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk+2-devel >= 2:2.18
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	libtool >= 1:1.4.3
%{?with_apidocs:BuildRequires:	xmlto}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	dbus-libs >= 0.76
Requires:	dbus-glib >= 0.76
Requires:	glib2 >= 1:2.6
Requires:	gtk+2 >= 2:2.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MATE Notifications library (used up to MATE 1.5.0). It's a fork of
pre-0.7 libnotify.

%description -l pl.UTF-8
Biblioteka powiadomień dla środowiska MATE (do wersji 1.5.0). Jest to
odgałęzienie libnotify sprzed wersji 0.7.

%package devel
Summary:	Development files for libmatenotify
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libmatenotify
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.76
Requires:	dbus-glib-devel >= 0.76
Requires:	glib2-devel >= 1:2.6
Requires:	gtk+2-devel >= 2:2.18

%description devel
Development files for libmatenotify.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki libmatenotify.

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
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mate-notify-send
%attr(755,root,root) %{_libdir}/libmatenotify.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmatenotify.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmatenotify.so
%{_includedir}/libmatenotify
%{_pkgconfigdir}/libmatenotify.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif
