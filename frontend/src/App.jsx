import React, { useEffect, useState } from 'react';
// import {
//   AppstoreOutlined,
//   ContainerOutlined,
//   DesktopOutlined,
//   MailOutlined,
//   MenuFoldOutlined,
//   MenuUnfoldOutlined,
//   PieChartOutlined,
// } from '@ant-design/icons';
import { Menu } from 'antd';
import axios from 'axios';
import productCard from '../components/productCard';

// const products = []

const App = () => {
  const [collapsed, setCollapsed] = useState(false);
  // const toggleCollapsed = () => {
  //   setCollapsed(!collapsed);
  // };
  const [products, setProducts] = useState([])

  const fetchProducts = () => {
    axios.get('http://127.0.0.1:8000/catalog/').then(response => {
      console.log('response', response)
      const productsResponse = response.data
      const menuItems = [
        {
          type: "group",
          label: "Продукты",
          children: productsResponse.map(c => {
               return {label: c.name, key: c.id}}),
        }
        // getItem('Список продуктов', 'g1', productsResponse.map(c => {
        //   return {label: c.name, key: c.id}
        // }))

      ]
      setProducts(menuItems)
    })
  }

  useEffect(() => {
    fetchProducts()
  }, [])

  return (
    <>
      <Menu
        style={{width: 256}}
        defaultSelectedKeys={['1']}
        defaultOpenKeys={['sub1']}
        mode="inline"
        theme="dark"
        inlineCollapsed={collapsed}
        items={products}/>
      <productCard/>
    </>
  );
};
export default App;