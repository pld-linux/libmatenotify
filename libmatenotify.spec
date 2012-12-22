Summary:	Libraries for mate notify
Name:		libmatenotify
Version:	1.5.0
Release:	0.1
License:	LGPL v2+
Group:		Libraries
URL:		http://mate-desktop.org/
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	28a1526c93f9a28a3cea9fdefbc47b41
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
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

find $RPM_BUILD_ROOT -name '*.la' |xargs rm

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
#%doc %{_datadir}/gtk-doc/html/libmatenotify/
%{_libdir}/libmatenotify.so
%{_pkgconfigdir}/libmatenotify.pc
%{_includedir}/libmatenotify

# -apidoc
%{_gtkdocdir}/libmatenotify
