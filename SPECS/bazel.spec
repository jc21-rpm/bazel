%undefine __brp_mangle_shebangs
%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

# Turn off strip'ng of binaries
%global __strip /bin/true

Name:           bazel
Version:        8.5.0
Release:        1%{?dist}
Summary:        a fast, scalable, multi-language and extensible build system
License:        Apache-2.0
URL:            https://bazel.build
Source0:        https://github.com/bazelbuild/bazel/releases/download/%{version}/bazel-%{version}-linux-x86_64

%description
%{summary}.

%install
install -Dm0644 %{SOURCE0} %{buildroot}/usr/bin/%{name}
chmod +x %{buildroot}/usr/bin/%{name}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}

%changelog
* Fri Dec 12 2025 Jamie Curnow <jc@jc21.com> - 8.5.0-1
- v8.5.0

* Thu Oct 2 2025 Jamie Curnow <jc@jc21.com> - 8.4.2-1
- v8.4.2

* Sat Sep 13 2025 Jamie Curnow <jc@jc21.com> - 8.4.1-1
- v8.4.1

* Fri Sep 5 2025 Jamie Curnow <jc@jc21.com> - 8.4.0-1
- v8.4.0

* Tue Jul 1 2025 Jamie Curnow <jc@jc21.com> - 8.3.1-1
- v8.3.1

* Tue Jun 24 2025 Jamie Curnow <jc@jc21.com> - 8.3.0-1
- v8.3.0

* Fri Apr 18 2025 Jamie Curnow <jc@jc21.com> - 8.2.1-1
- v8.2.1

* Tue Apr 15 2025 Jamie Curnow <jc@jc21.com> - 8.2.0-1
- v8.2.0

* Wed Feb 26 2025 Jamie Curnow <jc@jc21.com> - 8.1.1-1
- v8.1.1

* Mon Feb 24 2025 Jamie Curnow <jc@jc21.com> - 8.1.0-1
- v8.1.0
