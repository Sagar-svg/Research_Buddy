import React, {useState} from 'react'

const Searchform = ({onSearch}) => {

    const [search, setSearch] = useState('')

    const onSubmit = (e) => {
        e.preventDefault()
        if(!search){
            alert('Please enter in Search bar')
            return
        }
        console.log({search})
        onSearch({search})
       
    }


    return (
        <form className="add-form header" onSubmit={onSubmit}> 
            
            <div className='form-control'>
                
                <input type='text' placeholder='Add @youtubeSearch' value= {search} onChange={(e) => setSearch(e.target.value)}/>

            </div>
            <input type='submit' value='Search' className='btn' />
        </form>
    )
}

export default Searchform
