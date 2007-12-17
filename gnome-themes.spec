%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)
%define clearlooks 0.6.2

Summary: Themes for GNOME
Name: gnome-themes
Version: 2.21.2
Release: %mkrel 1
License: GPL
Group: Graphical desktop/GNOME
URL: http://www.gnome.org
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: http://prdownloads.sourceforge.net/clearlooks/clearlooks-%clearlooks.tar.bz2
# gw remove warnings about unsupported options
Patch: clearlooks-0.6.2-clearlooks-gtkrc-options.patch
Requires: gnome-icon-theme
BuildRequires: gtk-engines2 >= 2.9.0
BuildRequires:	libgnomeui2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:  icon-naming-utils >= 0.8.0
BuildRequires:  perl-XML-Parser
Conflicts: gtk-engines2 < 2.6
Conflicts: gnome-themes-extras <= 0.8.1-4mdk
Requires: gtk-engines2 >= 2.6
BuildArch: noarch

%description
This packages contains Themes for GNOME, such as :
- Clearlooks
- High Contrast
- Large Print
- Low Constrat

%prep
%setup -q -a 1
%patch

%build

./configure --prefix=%_prefix --libdir=%_libdir --enable-all-themes
cd clearlooks-%clearlooks
./configure --prefix=%_prefix --libdir=%_libdir

%make

%install
rm -rf $RPM_BUILD_ROOT
cd clearlooks-%clearlooks/themes
%makeinstall_std
cd ../..
%makeinstall_std GTK_BINARY_VERSION=%gtkbinaryver
#remove unpackaged files (not needed, since l10n is already in generated files)
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale 
# this is in gtk-engines2
rm -rf %buildroot%_datadir/themes/Clearlooks/gtk-2.0

for dir in %buildroot%{_datadir}/icons/*; do
 touch $dir/icon-theme.cache
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache Clearlooks
%update_icon_cache HighContrastInverse
%update_icon_cache LargePrint
%update_icon_cache Mist
%update_icon_cache Crux
%update_icon_cache HighContrastLargePrint
%update_icon_cache LowContrast
%update_icon_cache HighContrastLargePrintInverse 
%update_icon_cache LowContrastLargePrint
%update_icon_cache HighContrast
%update_icon_cache HighContrast-SVG

%postun
%clean_icon_cache Clearlooks
%clean_icon_cache HighContrastInverse
%clean_icon_cache LargePrint
%clean_icon_cache Mist
%clean_icon_cache Crux
%clean_icon_cache HighContrastLargePrint
%clean_icon_cache LowContrast
%clean_icon_cache HighContrastLargePrintInverse 
%clean_icon_cache LowContrastLargePrint
%clean_icon_cache HighContrast
%clean_icon_cache HighContrast-SVG

%files
%defattr(-,root,root,-)
%doc README NEWS AUTHORS 
%{_datadir}/themes/*
%dir %{_datadir}/icons/*
%{_datadir}/icons/*/??x??
%{_datadir}/icons/*/scalable
%{_datadir}/icons/Clearlooks/index.theme
%{_datadir}/icons/Crux/index.theme
%{_datadir}/icons/HighContrast-SVG/index.theme
%{_datadir}/icons/HighContrast/index.theme
%{_datadir}/icons/HighContrastInverse/index.theme
%{_datadir}/icons/HighContrastLargePrint/index.theme
%{_datadir}/icons/HighContrastLargePrintInverse/index.theme
%{_datadir}/icons/LargePrint/index.theme
%{_datadir}/icons/LowContrast/index.theme
%{_datadir}/icons/LowContrastLargePrint/index.theme
%{_datadir}/icons/Mist/index.theme
%ghost %{_datadir}/icons/*/icon-theme.cache
