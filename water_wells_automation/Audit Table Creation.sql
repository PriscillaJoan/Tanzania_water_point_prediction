CREATE TABLE wells_audit_log (
    log_id int primary key,
    well_id int,
    old_status varchar,
    new_status varchar,
    changed_at timestamp default current_timestamp
);

create or replace function log_well_update()
returns trigger as $$ 
begin
    if old.status is distinct from new.status then
        insert into wells_audit_log (well_id, old_status, new_status)
        values(old.well_id, old.status, new.status);
    end if;

    new.updated_at := current_timestamp;
    return new;
end;
$$ language plpgsql;

create trigger trigger_wells_update
before update on wells
for each row
execute function log_well_update();

