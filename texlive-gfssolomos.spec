# revision 18651
# category Package
# catalog-ctan /fonts/greek/gfs/gfssolomos
# catalog-date 2008-08-19 21:00:04 +0200
# catalog-license ofl
# catalog-version 1.0
Name:		texlive-gfssolomos
Version:	1.0
Release:	4
Summary:	A Greek-alphabet font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfssolomos
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Solomos is a font which traces its descent from a
calligraphically-inspired font of the mid-19th century. LaTeX
support, for use with the LGR encoding only, is provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gfssolomos/GFSSolomos-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfssolomos/gpsolomos.enc
%{_texmfdistdir}/fonts/map/dvips/gfssolomos/gfssolomos.map
%{_texmfdistdir}/fonts/opentype/public/gfssolomos/GFSSolomos.otf
%{_texmfdistdir}/fonts/tfm/public/gfssolomos/gsolomos8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfssolomos/gsolomos8r.tfm
%{_texmfdistdir}/fonts/type1/public/gfssolomos/GFSSolomos-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfssolomos/gsolomos8a.vf
%{_texmfdistdir}/tex/latex/gfssolomos/gfssolomos.sty
%{_texmfdistdir}/tex/latex/gfssolomos/lgrsolomos.fd
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/README
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/gfssolomos.pdf
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/gfssolomos.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752312
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718553
- texlive-gfssolomos
- texlive-gfssolomos
- texlive-gfssolomos

