# revision 18651
# category Package
# catalog-ctan /fonts/greek/gfs/gfssolomos
# catalog-date 2008-08-19 21:00:04 +0200
# catalog-license ofl
# catalog-version 1.0
Name:		texlive-gfssolomos
Version:	1.0
Release:	1
Summary:	A Greek-alphabet font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfssolomos
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Solomos is a font which traces its descent from a
calligraphically-inspired font of the mid-19th century. LaTeX
support, for use with the LGR encoding only, is provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}