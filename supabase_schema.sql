-- 1. App Users Table
create table app_users (
  id uuid primary key references auth.users(id) on delete cascade,
  email text,
  role text check (role in ('system_admin', 'police_officer', 'police_boss', 'license_accountant', 'license_coordinator'))
);

-- 2. Vehicles
create table vehicles (
  plate text primary key,
  make text,
  model text,
  year text,
  owner_name text
);

-- 3. Violations
create table violations (
  id uuid primary key default uuid_generate_v4(),
  plate text references vehicles(plate),
  added_by uuid references auth.users(id),
  violation_type text,
  fine_amount numeric,
  due_date date,
  status text check (status in ('pending', 'approved', 'cleared')) default 'pending',
  approved_by uuid references auth.users(id),
  cleared_by uuid references auth.users(id),
  created_at timestamp default now(),
  cleared_at timestamp
);

-- 4. Fines
create table fines (
  id uuid primary key default uuid_generate_v4(),
  violation_id uuid references violations(id),
  amount numeric,
  paid_at timestamp,
  paid_by uuid references auth.users(id),
  was_late boolean
);
