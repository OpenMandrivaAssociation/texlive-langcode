# revision 27764
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-langcode
Version:	20131019
Release:	3
Summary:	TeXLive langcode package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langcode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langcode.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langcode.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive langcode package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/langcode/langcode.sty
%doc %{_texmfdistdir}/doc/generic/langcode/README
%doc %{_texmfdistdir}/doc/generic/langcode/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/generic/langcode/langcode.pdf
#- source
%doc %{_texmfdistdir}/source/generic/langcode/langcode.tex
%doc %{_texmfdistdir}/source/generic/langcode/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
