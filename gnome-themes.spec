%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)
%define clearlooks 0.6.2
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Themes for GNOME
Name:		gnome-themes
Version:	2.32.1
Release:	10
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-themes/%{url_ver}/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/clearlooks/clearlooks-%{clearlooks}.tar.bz2
# gw remove warnings about unsupported options
Patch0:		clearlooks-0.6.2-clearlooks-gtkrc-options.patch
Patch1:		clearlooks-automake-1.13.patch
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk-engines-2)
BuildRequires:	pkgconfig(icon-naming-utils)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
Requires:	gnome-icon-theme
Requires:	gtk-engines2 >= 2.15.3

%description
This packages contains Themes for GNOME, such as :
- Clearlooks
- High Contrast
- Low Contrast

%prep
%setup -q -a 1
%apply_patches

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-all-themes
pushd clearlooks-%{clearlooks}
autoreconf -fi
./configure --prefix=%{_prefix} --libdir=%{_libdir}
popd

%make

%install
pushd clearlooks-%{clearlooks}/themes
%makeinstall_std
popd
%makeinstall_std GTK_BINARY_VERSION=%{gtkbinaryver}
#remove unpackaged files (not needed, since l10n is already in generated files)
rm -rf %{buildroot}%{_datadir}/locale 
# this is in gtk-engines2
rm -rf %{buildroot}%{_datadir}/themes/Clearlooks/gtk-2.0

for dir in %{buildroot}%{_iconsdir}/*; do
 touch $dir/icon-theme.cache
done

%post
%update_icon_cache Clearlooks
%update_icon_cache HighContrastInverse
%update_icon_cache LargePrint
%update_icon_cache Mist
%update_icon_cache Crux
%update_icon_cache HighContrastLargePrint
%update_icon_cache HighContrastLargePrintInverse 
%update_icon_cache HighContrast
%update_icon_cache HighContrast-SVG

%postun
%clean_icon_cache Clearlooks
%clean_icon_cache HighContrastInverse
%clean_icon_cache LargePrint
%clean_icon_cache Mist
%clean_icon_cache Crux
%clean_icon_cache HighContrastLargePrint
%clean_icon_cache HighContrastLargePrintInverse 
%clean_icon_cache HighContrast
%clean_icon_cache HighContrast-SVG

%files
%doc README NEWS AUTHORS 
%{_datadir}/themes/*
%dir %{_iconsdir}/*
%{_iconsdir}/*/??x??
%{_iconsdir}/*/???x???
%{_iconsdir}/*/scalable
%{_iconsdir}/Clearlooks/index.theme
%{_iconsdir}/Crux/index.theme
%{_iconsdir}/HighContrast-SVG/index.theme
%{_iconsdir}/HighContrast/index.theme
%{_iconsdir}/HighContrastInverse/index.theme
%{_iconsdir}/HighContrastLargePrint/index.theme
%{_iconsdir}/HighContrastLargePrintInverse/index.theme
%{_iconsdir}/LargePrint/index.theme
%{_iconsdir}/Mist/index.theme
%ghost %{_iconsdir}/*/icon-theme.cache

