from setuptools import setup, find_packages

setup(
    name="medgrid_theme",
    version="1.0.0",
    description="Medgrid Healthcare Network Theme for Frappe/ERPNext",
    author="Medgrid",
    author_email="admin@medgrid.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)
