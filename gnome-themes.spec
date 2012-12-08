%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)
%define clearlooks 0.6.2

Summary:	Themes for GNOME
Name:		gnome-themes
Version:	2.32.1
Release:	4
License:	LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/clearlooks/clearlooks-%{clearlooks}.tar.bz2
# gw remove warnings about unsupported options
Patch:		clearlooks-0.6.2-clearlooks-gtkrc-options.patch
Requires:	gnome-icon-theme
BuildRequires:	pkgconfig(gtk-engines-2)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	icon-naming-utils >= 0.8.0
BuildRequires:	intltool
Requires:	gtk-engines2 >= 2.15.3
BuildArch:	noarch

%description
This packages contains Themes for GNOME, such as :
- Clearlooks
- High Contrast
- Low Contrast

%prep
%setup -q -a 1
%patch -p0

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

for dir in %{buildroot}%{_datadir}/icons/*; do
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
%dir %{_datadir}/icons/*
%{_datadir}/icons/*/??x??
%{_datadir}/icons/*/???x???
%{_datadir}/icons/*/scalable
%{_datadir}/icons/Clearlooks/index.theme
%{_datadir}/icons/Crux/index.theme
%{_datadir}/icons/HighContrast-SVG/index.theme
%{_datadir}/icons/HighContrast/index.theme
%{_datadir}/icons/HighContrastInverse/index.theme
%{_datadir}/icons/HighContrastLargePrint/index.theme
%{_datadir}/icons/HighContrastLargePrintInverse/index.theme
%{_datadir}/icons/LargePrint/index.theme
%{_datadir}/icons/Mist/index.theme
%ghost %{_datadir}/icons/*/icon-theme.cache


%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 2.32.1-2mdv2011.0
+ Revision: 672455
- fix build
- fix patch apply

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Mon Nov 15 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 597840
- update to new version 2.32.1

* Wed Sep 29 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581973
- new version
- fix build

* Mon Aug 16 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 570575
- update to new version 2.31.90

* Tue Aug 03 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 565374
- update to new version 2.31.6

* Fri Jul 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.4-1mdv2011.0
+ Revision: 563401
- new version
- update file list

* Tue Jun 22 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2-1mdv2010.1
+ Revision: 548501
- Release 2.30.2

* Thu Apr 29 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 540765
- update to new version 2.30.1

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528964
- update to new version 2.30.0

* Mon Mar 08 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 516003
- update to new version 2.29.92

* Tue Feb 23 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509989
- update to new version 2.29.91

* Mon Jan 25 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 496283
- update to new version 2.29.6

* Wed Dec 09 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.2-1mdv2010.1
+ Revision: 475376
- update to new version 2.29.2

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458773
- Release 2.28.1

* Tue Sep 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 447373
- update to new version 2.28.0

* Thu Sep 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437480
- update to new version 2.27.92

* Mon Aug 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 420498
- update to new version 2.27.91

* Mon Aug 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414389
- update to new version 2.27.90

* Mon Jul 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 395711
- update to new version 2.27.4

* Mon Jun 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 386078
- update to new version 2.27.3

* Mon May 25 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 379674
- update to new version 2.27.2

* Mon May 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374194
- new version

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366929
- update to new version 2.26.1

* Tue Mar 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356665
- update to new version 2.26.0

* Mon Mar 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 347352
- update to new version 2.25.92

* Tue Feb 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341212
- update to new version 2.25.91

* Mon Feb 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336467
- update to new version 2.25.90

* Mon Jan 19 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 331324
- update to new version 2.25.5

* Thu Dec 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 315813
- update to new version 2.25.3

* Tue Dec 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 308991
- update to new version 2.25.2

* Tue Nov 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 299716
- update to new version 2.25.1

* Mon Oct 20 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295726
- update to new version 2.24.1

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286818
- new version

* Mon Sep 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282733
- new version

* Mon Sep 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278455
- new version

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273625
- new version
- bump deps

* Tue Aug 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263723
- new version

* Tue Jul 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.5-1mdv2009.0
+ Revision: 240066
- new version

* Thu Jul 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-3mdv2009.0
+ Revision: 233440
- rebuild again

* Thu Jul 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-2mdv2009.0
+ Revision: 233398
- rebuild with fixed icon-cache macros

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 230990
- new version
- update license

* Tue May 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 211623
- new version

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183685
- new version

* Mon Feb 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 174872
- new version

* Mon Feb 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165371
- new version

* Mon Jan 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 151656
- new version
- update file list

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.2-1mdv2008.1
+ Revision: 108391
- new version

* Mon Oct 29 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 103635
- new version
- new version

* Mon Oct 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98526
- new version

* Wed Sep 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 90942
- new version

* Mon Sep 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.92-1mdv2008.0
+ Revision: 78637
- new version

* Tue Aug 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91-3mdv2008.0
+ Revision: 72897
- remove warnings from old clearlooks themes

* Tue Aug 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91-2mdv2008.0
+ Revision: 72730
- don't overwrite Clearlooks theme file with old version

* Tue Aug 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 72706
- new version

* Tue Aug 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 63024
- new version

* Mon Jul 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 56532
- new version

* Mon Jul 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 50625
- new version
- new version

* Tue Apr 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 14037
- new version


* Tue Mar 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142142
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Tue Feb 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 126211
- new version

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 120016
- new version

* Mon Jan 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 111948
- new version

* Tue Dec 19 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.4-1mdv2007.1
+ Revision: 99081
- new version
- bump deps

* Tue Dec 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.3-1mdv2007.1
+ Revision: 90724
- new version

* Mon Nov 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2-1mdv2007.1
+ Revision: 87625
- new version

* Wed Nov 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.2-1mdv2007.1
+ Revision: 86298
- new version

* Tue Nov 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1.1-3mdv2007.0
+ Revision: 77288
- reupload missing package
- fix gtkbinaryver macro
- mkrel
- Import gnome-themes

* Sat Oct 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1.1-1
- New version 2.16.1.1

* Wed Oct 04 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-1
- New version 2.16.1

* Wed Sep 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New version 2.16.0

* Sat Sep 02 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- rebuild for new clean_icon_cache macro

* Thu Aug 31 2006 Götz Waschk <waschk@mandriva.org> 2.15.92-2mdv2007.0
- fix uninstallation

* Tue Aug 22 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.92-1mdv2007.0
- Release 2.15.92

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.91.1-1mdv2007.0
- New release 2.15.91.1

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- update file list
- fix buildrequires
- New release 2.15.91

* Fri Jul 28 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-2mdv2007.0
- fix uninstallation

* Wed Jul 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.90-1
- New release 2.15.90

* Tue Jul 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- New release 2.15.4

* Wed Jun 14 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.3-1
- New release 2.15.3

* Fri Jun 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.2-1mdv2007.0
- Release 2.15.2

* Tue May 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- New release 2.14.2

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.0-1mdk
- Release 2.14.0

* Mon Feb 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-1mdk
- New release 2.12.3
- use mkrel

* Sun Oct 09 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-3mdk
- don't delete the metacity theme

* Thu Oct 06 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-2mdk
- add clearlooks alternative themes and icons

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdk
- Release 2.12.1

* Thu Jun 23 2005 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- New release 2.10.2

* Tue Apr 19 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-1mdk 
- Release 2.10.1, based on Götz Waschk package

* Mon Dec 27 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.2-2mdk
- this is now noarch
- remove files that were moved to gtk-engines2

* Sat Dec 04 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.8.2-1mdk
- New release 2.8.2

* Wed Oct 20 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-1mdk
- New release 2.8.0

* Fri Jun 25 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.3-1mdk
- reenable libtoolize
- New release 2.6.3

* Wed Jun 09 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- New release 2.6.2

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.1-2mdk
- Fix BuildRequires

* Wed Apr 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.1-1mdk
- New release 2.6.1

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- Release 2.6.0 (with Götz Waschk help)

* Tue Apr 06 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.4.1-2mdk
- rebuild for gtk+-2.4 (because of theme engines path)

