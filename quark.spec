#
# todo:
# - should cli client link with gtk+ libraries?
# - strange-quark separate package (first, resolve first todo item)?
#
Summary:	Quark is an audio player, for geeks, by geeks
Summary(pl):	Quark to odtwarzacz d¼wiêku pisany przez geeków dla geeków
Name:		quark
Version:	3.11
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://quark.nerdnest.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-schemas.patch
# Source0-md5:	938467f152ef4815caddcbcd32ab478d
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	xine-lib-devel
Requires(post):	GConf2
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quark is an audio player, for geeks, by geeks. It runs in the
background with access provided via a FIFO in the filesystem. It uses
Xine-lib for playing music, and can therefore play any file format
supported by Xine.

%description -l pl
Quark to odtwarzacz d¼wiêku pisany przez geeków dla geeków. Dzia³a w
tle z dostêpem przez nazwany potok umieszczony w systemie plików. Do
odtwarzania muzyki u¿ywa Xine-lib, wiêc mo¿e odtwarzaæ pliki w
dowolnym formacie obs³ugiwanym przez Xine.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
%gconf_schema_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/charm-quark
%attr(755,root,root) %{_bindir}/quark
%attr(755,root,root) %{_bindir}/strange-quark
%{_sysconfdir}/gconf/schemas/*.schemas
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
