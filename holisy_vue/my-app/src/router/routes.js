export default [
    //Fallback route
    // {
    //   path: '/',
    //   redirect: {
    //     path: '/login',
    //   },
    // },
  
    {
      path: '/',
      name: 'homepage',
      meta: { layout: 'public_layout' },
      component: () => import('@/views/publicComponents/homepage/index.vue'),
    },
    
    {
      path: '/login',
      name: 'login',
      meta: { layout: 'authorization' },
      component: () => import('@/views/publicComponents/authorization/Login.vue'),
    },

    {
      path: '/signup',
      name: 'signup',
      meta: { layout: 'authorization' },
      component: () => import('@/views/publicComponents/authorization/Signup.vue'),
    },

    {
      path: '/admin',
      redirect: {
        path: '/admin/users',
      },
    },

    {
      path: '/admin/users',
      name: 'admin_users',
      meta: { layout: 'admin_panel' },
      component: () => import('@/views/adminComponents/panel/Users.vue'),
    },

    {
      path: '/admin/rooms',
      name: 'admin_rooms',
      meta: { layout: 'admin_panel' },
      component: () => import('@/views/adminComponents/panel/Rooms.vue'),
    },

    {
      path: '/admin/services',
      name: 'admin_services',
      meta: { layout: 'admin_panel' },
      component: () => import('@/views/adminComponents/panel/Services.vue'),
    },

    {
      path: '/admin/bookings',
      name: 'admin_bookings',
      meta: { layout: 'admin_panel' },
      component: () => import('@/views/adminComponents/panel/Bookings.vue'),
    },

    {
      path: '/admin/applications',
      name: 'admin_applications',
      meta: { layout: 'admin_panel' },
      component: () => import('@/views/adminComponents/panel/Applications.vue'),
    },

    {
      path: '/room/:id',
      name: 'oneRoom',
      meta: { layout: 'public_layout' },
      component: () => import('@/views/publicComponents/homepage/OneRoom.vue'),
    },
  
    {
      path: '*',
      name: 'error',
      meta: { layout: 'public_layout', requiresAuth: false },
      component: () => import('@/views/publicComponents/notfound/index.vue'),
    },
  ];
  