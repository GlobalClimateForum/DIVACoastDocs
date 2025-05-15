# DIVACoast.jl Documentation

> [!IMPORTANT]
> This is the repository for the DIVACoast.jl Doumentation and **not the actual package**. You can find the actual package here: [DIVACoast.jl](https://github.com/GlobalClimateForum/DIVACoast.jl)

## Workflow to update DIVACoast.jl Documentation

### Document Functions
Functions within the code are documented by a docstring above the function name, like:
```julia
"""
    function doSomething(x::something)
First a small function description for the function `doSomething()` that does something.

# Arguments
- **something**: explain what the `something` argument does

# Returns
The function returns something of type something

# Example
example (use markdown codeblock)
"""
function doSomething(x::something)
  println(something)
  return something
end
```

### Add docstring to documentation
The documentation is stored in the `DIVACoast.jl` repository `docs/build` folder. Each `.md`file corresponds to a page in the documentation. In the .md file
you can link function documentations by using docstrings and the `@docs` macro. Within the docstring you can link the docstrings from your code by using the **full** name.
of the function. 

```markdown
\```@docs
Main.DIVACoast.doSomething
\```
```

### Create HTML
After editing the `.md` files run the `make.jl` script to generate a html version of the documentation. Push the changes (the new html file + additions) to the `DIVACoast.jl` repository. 

### Update Online Version
After pushing the changes you made you can update the online version of the documentation. Switch to this repository `DIVACoastDocs` and pull the latest changes of the `DIVACoast.jl` submodule by:

```bash
git submodule update --remote --merge
```
The changes will appear after some time. Sometimes you need to `hard refresh` the page in you browser to see the changes!

### Changes in documentation wrapper
If you want to make changes in the documentation wrapper (everything around the documentation html) you can use a local development server by running the 
`devServer.py` Python file and opening `localhost:8000` in your browser.
