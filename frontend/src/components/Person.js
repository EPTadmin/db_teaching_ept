import React from 'react';
import { useEffect } from 'react';
import AxiosInstance from './Axios';
import { useState } from 'react';
import { useMemo } from 'react';
import { MaterialReactTable } from 'material-react-table';
import { Box } from '@mui/material';
import { IconButton } from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon } from '@mui/icons-material';
import {Link} from 'react-router-dom';


const Person = () => {
    const[myData, setMydata]=useState()
    const[loading,setLoading] = useState(true)


     const GetData = () => {
        AxiosInstance.get(`person/`).then((res) => {
           setMydata(res.data) 
           console.log(res.data)
           setLoading(false)
    })


     }
    useEffect(() => { 

        GetData();
   
    },[])





   
      const columns = useMemo(
        () => [
          {
            accessorKey: 'first_name',
            header: 'First Name',
            size: 150,
          },
          {
            accessorKey: 'last_name',
            header: 'Last Name',
            size: 150,
          },
          {
            accessorKey: 'position', //normal accessorKey
            header: 'Position',
            size: 80,
          },
          {
            accessorKey: 'groupe',
            header: 'Group',
            size: 80,
          },



          {
            accessorKey: 'courses',
            header: 'Courses',
            size: 150,
          },
          {
            accessorKey: 'activities',
            header: 'Activities',
            size: 80,
          },
          
        

        ],
        [],
      );
    

    
      



    return(
        <div>
            { loading ? <p>Loading data ...</p> :
            <MaterialReactTable 
                columns={columns} 
                data={myData}
                enableRowActions
                renderRowActions={({row}) => (
                    <Box sx={{ display: 'flex', flexWrap: 'nowrap', gap: '8px' }}>

                    <IconButton color="secondary" component = {Link} to={`edit_person/${row.original.id}`}>
                        <EditIcon />
                    </IconButton>

                    <IconButton color="error" component = {Link} to={`delete_person/${row.original.id}`}>
                        <DeleteIcon />
                    </IconButton>
                    </Box>
      )}

            />
        }
        </div>
        
    )
}



export default Person