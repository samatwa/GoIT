import axios from 'axios';
import { createAsyncThunk } from '@reduxjs/toolkit';
import toast from 'react-hot-toast';

axios.defaults.baseURL = 'https://connections-api.goit.global/';

export const fetchContacts = createAsyncThunk('contacts/fetchAll', async (_, thunkAPI) => {
  try {
    const { data } = await axios.get('/contacts');
    return data;
  } catch (error) {
    return thunkAPI.rejectWithValue(error.message);
  }
});

export const addContact = createAsyncThunk('contacts/addContact', async (contact, thunkAPI) => {
  try {
    const { data } = await axios.post('/contacts', contact);
    toast.success(`Contact "${data.name}" added!`);
    return data;
  } catch (error) {
    toast.error('Failed to add contact');
    return thunkAPI.rejectWithValue(error.message);
  }
});

export const deleteContact = createAsyncThunk(
  'contacts/deleteContact',
  async (id, thunkAPI) => {
    try {
      const { data } = await axios.delete(`/contacts/${id}`);
      toast.success(`Contact "${data.name}" deleted!`);
      return data;
    } catch (error) {
      toast.error('Failed to delete contact');
      return thunkAPI.rejectWithValue(error.message);
    }
  }
);

export const updateContact = createAsyncThunk(
  'contacts/updateContact',
  async ({ id, updatedData }, thunkAPI) => {
    try {
      const res = await axios.patch(`/contacts/${id}`, updatedData);
      toast.success(`Contact "${res.data.name}" updated!`);
      return res.data;
    } catch (error) {
      toast.error('Failed to update contact');
      return thunkAPI.rejectWithValue(error.message);
    }
  }
);